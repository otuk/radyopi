# -*- coding: utf-8 -*-

import pygame

class Glasspanel(pygame.sprite.Sprite):
    
    def __init__(self, config, gs):
        super().__init__()
        self.image = pygame.image.load(config.glasspanel["image"])
        self.image = pygame.transform.scale(self.image,(config.glasspanel["width"],
                                                        config.glasspanel["height"]))
        self.rect = self.image.get_rect()
        self.rect.x = -8
        self.rect.y = -2



        
