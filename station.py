# -*- coding: utf-8 -*-


import pygame
import subprocess

import indicator


class Station(pygame.sprite.Sprite):

    ANTIALIAS_YES = 1
    
    def __init__(self, config, stano, col, row, starts_at, ind_starts_at, ig):
        super().__init__()
        #c.debug("station ", stano, "col:",col, "row:",row, "starts_at:",starts_at )
        self.config = config
        self.active = False
        self.no = stano
        self.row = row
        self.col = col
        self.name = config.stations[self.no]["name"]
        self.url = config.stations[self.no]["url"]
        self.region = config.stations[self.no]["region"]
        self.statype = config.stations[self.no]["type"]
        myfont = pygame.font.SysFont(self.config.sta_display["font"],
                                     self.config.sta_display["font_size"])
        self.inactiveimg = myfont.render(self.name, Station.ANTIALIAS_YES, 
                                         self.config.sta_display["inactive_color"])
        self.activeimg = myfont.render(self.name, Station.ANTIALIAS_YES, 
                                       self.config.sta_display["active_color"])
        self.set_image()
        self.rect = self.image.get_rect()
        self.delta = 0
        self._x = max(starts_at, ind_starts_at) 
        self.rect.x = self._x + self.delta
        self._y = self.config.sta_display["gap_y"] + self.row * (self.config.sta_display["height"] + self.config.sta_display["gap_y"])
        self.rect.y = self._y + self.delta
        #c.debug(self.rect)
        self.ind = indicator.Indicator(config, self, self.rect.centerx -20, self.rect.centery+ 10)
        ig.add(self.ind)
        
        
    def set_image(self):
        if self.active:
            self.image = self.activeimg
        else:
            self.image = self.inactiveimg
        
        
        
    def set_active(self, active):
       if active != self.active and active:
           self.active = active
           subprocess.call("mpc play " + str(self.no + 1), shell=True)
           self.set_image()
       elif active != self.active and not active:            
           self.active = active
           subprocess.call("mpc stop ", shell=True)
           self.set_image()
       
       
    def set_delta(self,d):
        self.delta = d
        self.ind.set_delta(d)

        
    def get_width(self):        
        return self.rect.width

    
    def get_height(self):        
        return self.rect.height

    def ends_at(self):
        return self._x + self.get_width() 
 
    def iends_at(self):
        return self.ind.ends_at()

    
    def update(self):
        self.rect.x = self._x + self.delta

        
