# -*- coding: utf-8 -*-

import datetime
import pygame
import feedparser

class Clock(pygame.sprite.Sprite):

    ANTIALIAS_YES = True
    UPDATEEVERY = 15 # seconds
    UPDATENEWS = 2 # times  
    
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.largefont = pygame.font.SysFont(self.config.clock["font"],
                                     self.config.clock["font_size_L"])
        largefont.set_bold(True)
        self.mediumfont = pygame.font.SysFont(self.config.clock["font"],
                                     self.config.clock["font_size_M"])
        self.smallfont = pygame.font.SysFont(self.config.clock["font"],
                                     self.config.clock["font_size_S"])
        Clock.UPDATEEVERY = Clock.UPDATEEVERY * config.FPS;        
        self.counter = Clock.UPDATEEVERY
        self.newscounter = 0
        self.prepare_img()

        
    def prepare_img(self):
        self.time = datetime.datetime.now().strftime("%I:%M")
        self.ampm = datetime.datetime.now().strftime("%p")
        self.date = datetime.datetime.now().strftime("%B %d - %A")
        timeimg = self.largefont.render(self.time, Clock.ANTIALIAS_YES, 
                                         self.config.clock["color"])
        self.bgimg = pygame.image.load(self.config.clock["image"])
        #self.bgimg = pygame.transform.scale(self.bgimg,(self.config.width,
        #                                              self.config.height))
        rect = timeimg.get_rect()
        rect.centerx = self.config.width // 2 - 20
        ampmimg = self.mediumfont.render(self.ampm, Clock.ANTIALIAS_YES, 
                                         self.config.clock["color"])
        dateimg = self.smallfont.render(self.date, Clock.ANTIALIAS_YES, 
                                         self.config.clock["color"])
        self.bgimg.blit(timeimg,(rect.x, 10))
        self.bgimg.blit(ampmimg,(rect.x+rect.w +5 , 40))
        self.bgimg.blit(dateimg,(rect.x + 20, 80))
        self.newscounter += 1
        if self.newscounter % Clock.UPDATENEWS == 0 :
            self.printnews()
            self.newscounter = 0;
        self.image = self.bgimg
        self.rect = self.image.get_rect()
        self.rect.centerx = self.config.width // 2
            

        
    def update(self):
        self.counter -= 1
        if self.counter <= 0:
            self.counter = Clock.UPDATEEVERY
            self.prepare_img()


        
    def printnews(self):
        d = feedparser.parse('http://feeds.bbci.co.uk/news/rss.xml?edition=us')
        nt = d.entries[0]["title"]
        newimg = self.smallfont.render(nt, Clock.ANTIALIAS_YES, 
                                         self.config.clock["color"])
        self.bgimg.blit(newimg,(rect.x + 10, 100))
