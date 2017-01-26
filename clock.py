# -*- coding: utf-8 -*-

import datetime
import pygame

class Clock(pygame.sprite.Sprite):

    ANTIALIAS_YES = True
    UPDATEEVERY = 15 # seconds 
    
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.prepare_img()
        self.rect.centery = config.height // 2
        Clock.UPDATEEVERY = Clock.UPDATEEVERY * config.FPS;        
        self.counter = Clock.UPDATEEVERY
        

    def prepare_img(self):
        self.time = datetime.datetime.now().strftime("%I:%M")
        self.ampm = datetime.datetime.now().strftime("%p")
        self.date = datetime.datetime.now().strftime("%B %d - %A")
        largefont = pygame.font.SysFont(self.config.clock["font"],
                                     self.config.clock["font_size_L"])
        largefont.set_bold(True)
        mediumfont = pygame.font.SysFont(self.config.clock["font"],
                                     self.config.clock["font_size_M"])
        smallfont = pygame.font.SysFont(self.config.clock["font"],
                                     self.config.clock["font_size_S"])
        timeimg = largefont.render(self.time, Clock.ANTIALIAS_YES, 
                                         self.config.clock["color"])
        self.bgimg = pygame.image.load(self.config.clock["image"])
        self.bgimg = pygame.transform.scale(self.bgimg,(self.config.width,
                                                      self.config.height))
        rect = timeimg.get_rect()
        rect.centerx = self.config.width // 2 - 20
        ampmimg = mediumfont.render(self.ampm, Clock.ANTIALIAS_YES, 
                                         self.config.clock["color"])
        dateimg = smallfont.render(self.date, Clock.ANTIALIAS_YES, 
                                         self.config.clock["color"])
        self.bgimg.blit(timeimg,(rect.x, 0))
        self.bgimg.blit(ampmimg,(rect.x+rect.w, 40))
        self.bgimg.blit(dateimg,(rect.x + 50, 80))
        self.image = self.bgimg
        self.rect = self.image.get_rect()
        self.rect.centerx = self.config.width // 2
            

        

    def update(self):
        self.counter -= 1
        if self.counter == 0:
            self.counter = Clock.UPDATEEVERY
            self.prepare_img()


        
