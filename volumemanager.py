# -*- coding: utf-8 -*-



import subprocess
import pygame

class VolumeManager(pygame.sprite.Sprite):

    
    def __init__(self, config, gs):
        super().__init__()
        self.config = config
        self.gs = gs
        self._vol = gs.get_last_vol()
        self.min = config.volume["min_vol"]
        self.max = config.volume["max_vol"]
        self.increment = config.volume["increment"]
        self.vol = 0
        self.premutevol = self._vol
        self._clear = False
        self.set_volume(self._vol)

        

        
    def set_volume(self, v):
        if v > self.max:
            self._vol = self.max
        elif self._vol < self.min:
            self._vol = self.min
        else :
            self._vol = v


            
    def increase_volume(self, v):
        self._vol += v
        if self._vol > self.max:
            self._vol = self.max

            

    def lower_volume(self, v):
        self._vol -= v
        if self._vol < self.min:
            self._vol = self.min

            

    def mute(self):
        self.premutevol = self._vol
        self.set_volume(0)

        

    def unmute(self):
        self.set_volume(self.premutevol)


        
    def clear(self):
        self._clear = True    

        

    def kill_mpc(self): 
        subprocess.call("mpc stop ", shell=True)
        subprocess.call("mpc clear ", shell=True)
        subprocess.call("mpc rm  "
                        + self.config.sta_manager["playlist_name"], shell=True)           
        

    def update(self):
        if self._clear:
            self.kill_mpc()
            self._clear = False
        if self.vol != self._vol:
            subprocess.call("mpc volume "+str(self._vol), shell=True)
            self.vol = self._vol
