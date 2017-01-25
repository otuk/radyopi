# -*- coding: utf-8 -*-

import datetime
import pygame

class Clock(pygame.sprite.Sprite):

    ANTIALIAS_YES = True
    UPDATEEVERY = 10 # seconds 
    
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.prepare_img()
        self.rect.centery = config.height // 2
        Clock.UPDATEEVERY = Clock.UPDATEEVERY * config.FPS;        
        self.counter = Clock.UPDATEEVERY
        

    def prepare_img(self):
        self.time = datetime.datetime.now().strftime("%I:%M %p")
        self.date = datetime.datetime.now().strftime("%B %d - %A")
        myfont = pygame.font.SysFont(self.config.clock["font"],
                                     self.config.clock["font_size"])
        myfont.set_bold(True)
        img = myfont.render(self.time, Clock.ANTIALIAS_YES, 
                                         self.config.clock["color"])
        img = pygame.transform.scale(img, (self.config.clock["width"],
                                          self.config.clock["height"]) )
        self.bgimg = pygame.image.load(self.config.clock["image"])
        self.bgimg = pygame.transform.scale(self.bgimg,(self.config.width,
                                                        self.config.height))
        rect = img.get_rect()
        rect.centerx = self.config.width // 2
        self.bgimg.blit(img,(rect.x, 5))
        self.image = self.bgimg
        self.rect = self.image.get_rect()
        self.rect.centerx = self.config.width // 2
            

        

    def update(self):
        self.counter -= 1
        if self.counter == 0:
            self.counter = Clock.UPDATEEVERY
            self.prepare_img()
        

        
