# -*- coding: utf-8 -*-

import pygame

class Indicator(pygame.sprite.Sprite):
    
    def __init__(self, config, sta, x, y):
        super().__init__()
        self.config = config
        self.inactiveimage = pygame.Surface((30,10)) #TODO use config info
        self.inactiveimage.set_colorkey((0,0,0))  # this is ugly
        pygame.draw.ellipse(self.inactiveimage, (190,190,190), (0, 0, 30,10))
        self.activeimage = pygame.Surface((30,10))
        self.activeimage.set_colorkey((0,0,0))  # this is ugly
        pygame.draw.ellipse(self.activeimage, (250,70, 0), (0, 0, 30,10))
        self.image = self.inactiveimage
        self.rect = self.image.get_rect()
        self.delta = 0
        self._x = x
        self._y = y
        self.rect.x = self._x + self.delta
        self.rect.y = self._y
        self.sta = sta


    def set_delta(self, d):
        self.delta = d

   
    def ends_at(self):
        return self._x + self.get_width() 

    def get_width(self):        
        return self.rect.width
    
        
    def update(self):
        self.rect.x = self._x + self.delta
        if self.rect.collidepoint(self.config.width//2, self.rect.centery):
            self.image = self.activeimage
            self.sta.set_active(True)
        else:
            self.image = self.inactiveimage
            self.sta.set_active(False)
        
