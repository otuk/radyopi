# -*- coding: utf-8 -*-

import pygame

class Background(pygame.sprite.Sprite):
    
    def __init__(self, config, gs):
        super().__init__()
        self.image = pygame.image.load(config.image)
        self.image = pygame.transform.scale(self.image,(config.width, config.height))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0



        
