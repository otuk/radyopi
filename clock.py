# -*- coding: utf-8 -*-

import datetime
import pygame
import feedparser

import common as c

class Clock(pygame.sprite.Sprite):
    """
    Shows the time -date
    And also fetches news from news outlet(BBC) and parses
    """
    ANTIALIAS_YES = True
    UPDATEEVERY = 5 # seconds
    UPDATENEWS = 3 # times  

    def __init__(self, config):
        super().__init__()
        #c.debug("init new clock")
        self.config = config
        self.newssource = self.config.clock["news_source"]
        self.bgcolor = self.config.clock["background_color"]
        self.largefont = pygame.font.SysFont(self.config.clock["font"],
                                     self.config.clock["font_size_L"])
        self.largefont.set_bold(True)
        self.mediumfont = pygame.font.SysFont(self.config.clock["font"],
                                     self.config.clock["font_size_M"])
        self.smallfont = pygame.font.Font("OxygenMono-Regular.otf", 
                                     self.config.clock["font_size_S"])
        self.xsmallfont = pygame.font.SysFont(self.config.clock["font"],
                                     self.config.clock["font_size_XS"])
        self.updatefreq = Clock.UPDATEEVERY * config.FPS        
        self.updatecounter = self.updatefreq
        self.newsfetchcounter = 0
        self.newscounter = 0
        self.newslength = 0
        self.prepare_image()
        #c.debug("new clock created")

        
    def prepare_image(self):
        #c.debug("updating clock image")
        self.newsfetchcounter -= 1
        if self.newsfetchcounter <= 0 :
            self.bgimg = pygame.image.load(self.config.clock["image"])
            self.print_news()
            self.newsfetchcounter = Clock.UPDATENEWS
        self.time = datetime.datetime.now().strftime("%I:%M")
        self.ampm = datetime.datetime.now().strftime("%p")
        self.date = datetime.datetime.now().strftime("%B %d - %A")
        timeimg = self.largefont.render(self.time, Clock.ANTIALIAS_YES, 
                                         self.config.clock["color"], self.bgcolor)
        rect = timeimg.get_rect()
        rect.centerx = self.config.width // 2 - 20
        ampmimg = self.mediumfont.render(self.ampm, Clock.ANTIALIAS_YES, 
                                         self.config.clock["color"], self.bgcolor)
        dateimg = self.xsmallfont.render(self.date, Clock.ANTIALIAS_YES, 
                                         self.config.clock["color"], self.bgcolor)
        self.bgimg.blit(timeimg,(rect.x, 10))  # TODO magic numbers for formating move to settings
        self.bgimg.blit(ampmimg,(rect.x+rect.w +5 , 40))
        self.bgimg.blit(dateimg,(rect.x + 20, 80))
        self.image = self.bgimg
        self.rect = self.image.get_rect()
        self.rect.centerx = self.config.width // 2
            

        
    def update(self):
        #c.debug("clock update called", self.counter)
        self.updatecounter -= 1
        if self.updatecounter <= 0:
            self.updatecounter = self.updatefreq
            self.prepare_image()


        
    def print_news(self):
        if self.newscounter < self.newslength:
            #c.debug("printing news on screen ", self.newscounter)
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
            #c.debug("getting news")
            self.newsdata = feedparser.parse(self.newssource)
            self.newslength = len(self.newsdata.entries)
            #c.debug("news len ",self.newslength)
            self.newscounter = 0


    def format_text(self, text, txtfont, xstart, ystart, ystep, cwidth, baseimg):
        """
        Makes sure text fits in space, with multi-lines 
        """
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
            
