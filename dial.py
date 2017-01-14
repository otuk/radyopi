# -*- coding: utf-8 -*-

import pygame

class Dial(pygame.sprite.Sprite):
    
    def __init__(self, config, gs):
        super().__init__()
        self.image = pygame.image.load(config.dial["image"])
        self.image = pygame.transform.scale(self.image,(config.dial["width"],
                                                        config.dial["height"]))
        self.rect = self.image.get_rect()
        self.delta = 0
        self._x = config.width // 2
        self._y = 0
        self.rect.x = self._x + self.delta
        self.rect.y = self._y 


    def add_delta(self, d):
        self.delta += d

    def update(self):
        if self.rect.x < self._x:
            self.delta += 1
        elif self.rect.x > self._x:
            self.delta += -1
        self.rect.x = self._x + self.delta

        
        
