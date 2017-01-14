# -*- coding: utf-8 -*-



import subprocess
import pygame

class VolumeManager(pygame.sprite.Sprite):

    def __init__(self, config):
        super().__init__()
        self.config = config
        self._vol = 50
        self.vol = 0
        self.premutevol = self._vol
        self._clear = False
        self.set_volume(self._vol)

        

        
    def set_volume(self, v):
        if v > 100:
            self._vol = 100
        elif self._vol < 0:
            self._vol = 0
        else :
            self._vol = v


            
    def increase_volume(self, v):
        self._vol += v
        if self._vol > 100:
            self._vol = 100

            

    def lower_volume(self, v):
        self._vol -= v
        if self._vol < 0:
            self._vol = 0

            

    def mute(self):
        self.premutevol = self._vol
        self.set_volume(0)

        

    def unmute(self):
        self.set_volume(self.premutevol)


        
    def clear(self):
        self._clear = True    

        

    def update(self):
        if self._clear:
            subprocess.call("mpc clear ", shell=True)
            subprocess.call("mpc rm  "
                            + self.config.sta_manager["playlist_name"], shell=True)            
            self._clear = False
        if self.vol != self._vol:
            subprocess.call("mpc volume "+str(self._vol), shell=True)
            self.vol = self._vol
