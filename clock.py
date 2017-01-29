# -*- coding: utf-8 -*-

import datetime
import pygame
import feedparser

class Clock(pygame.sprite.Sprite):

    ANTIALIAS_YES = True
    UPDATEEVERY = 3 # seconds
    UPDATENEWS = 2 # times  
    
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.largefont = pygame.font.SysFont(self.config.clock["font"],
                                     self.config.clock["font_size_L"])
        self.largefont.set_bold(True)
        self.mediumfont = pygame.font.SysFont(self.config.clock["font"],
                                     self.config.clock["font_size_M"])
        self.smallfont = pygame.font.Font("OxygenMono-Regular.otf", #self.config.clock["font"],
                                     self.config.clock["font_size_S"])
        self.xsmallfont = pygame.font.SysFont(self.config.clock["font"],
                                     self.config.clock["font_size_XS"])
        Clock.UPDATEEVERY = Clock.UPDATEEVERY * config.FPS;        
        self.counter = Clock.UPDATEEVERY
        self.newsfetchcounter = 0
        self.newscounter = 0
        self.newslength = 0
        self.prepare_img()

        
    def prepare_img(self):
        self.time = datetime.datetime.now().strftime("%I:%M")
        self.ampm = datetime.datetime.now().strftime("%p")
        self.date = datetime.datetime.now().strftime("%B %d - %A")
        timeimg = self.largefont.render(self.time, Clock.ANTIALIAS_YES, 
                                         self.config.clock["color"])
        self.bgimg = pygame.image.load(self.config.clock["image"])
        rect = timeimg.get_rect()
        rect.centerx = self.config.width // 2 - 20
        ampmimg = self.mediumfont.render(self.ampm, Clock.ANTIALIAS_YES, 
                                         self.config.clock["color"])
        dateimg = self.xsmallfont.render(self.date, Clock.ANTIALIAS_YES, 
                                         self.config.clock["color"])
        self.bgimg.blit(timeimg,(rect.x, 10))
        self.bgimg.blit(ampmimg,(rect.x+rect.w +5 , 40))
        self.bgimg.blit(dateimg,(rect.x + 20, 80))
        self.newsfetchcounter += 1
        if self.newsfetchcounter % Clock.UPDATENEWS == 0 :
            self.printnews()
            self.newsfetchcounter = 0;
        self.image = self.bgimg
        self.rect = self.image.get_rect()
        self.rect.centerx = self.config.width // 2
            

        
    def update(self):
        self.counter -= 1
        if self.counter <= 0:
            self.counter = Clock.UPDATEEVERY
            self.prepare_img()


        
    def printnews(self):
        if self.newscounter < self.newslength:
            nt = self.newsdata.entries[self.newscounter]["title"]
            ns = self.newsdata.entries[self.newscounter]["summary"]
            ystep = 24
            xstart = 4
            cwidth = 41
            ystart = self.format_text(nt, self.smallfont, xstart, ystart=104,
                                      ystep=ystep, cwidth=cwidth, baseimg=self.bgimg)    

            ystart = self.format_text(ns, self.smallfont, xstart, ystart=ystart+ystep//2,
                                      ystep=ystep, cwidth=cwidth, baseimg=self.bgimg)    
            self.newscounter += 1
        else:
            print("getting news")
            self.newsdata = feedparser.parse(
                'http://feeds.bbci.co.uk/news/rss.xml?edition=us')
            self.newslength = len(self.newsdata.entries)
            print("news len ",self.newslength)
            self.newscounter = 0


            
    def format_text(self, text, txtfont, xstart, ystart, ystep, cwidth, baseimg):
            textli = text.split()
            maxsl = cwidth
            slen = 0
            line = []
            yshift = 0
            for w in textli:
                if slen+len(w) < maxsl:
                    line.append(w+" ")
                    slen += len(w) +1
                else:
                    titimg = txtfont.render( ''.join(line), 
                                             Clock.ANTIALIAS_YES,
                                             self.config.clock["color"])
                    baseimg.blit(titimg, (xstart, ystart + yshift))
                    slen = len(w)+1
                    line = [w+" "]
                    yshift += ystep
            if len(line) > 0:
                titimg = txtfont.render( ''.join(line), 
                                         Clock.ANTIALIAS_YES,
                                         self.config.clock["color"])
                baseimg.blit(titimg, (xstart, ystart + yshift))
            return ystart + yshift + ystep
            
