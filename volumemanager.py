# -*- coding: utf-8 -*-


import subprocess
import pygame

import importlib

mRPi = importlib.find_loader("RPi")
RUNNING_ON_PI = mRPi is not None
if RUNNING_ON_PI:
    import r_buttonhandler as rbh



class VolumeManager(pygame.sprite.Sprite):

    
    def __init__(self, config, gamestats):
        super().__init__()
        self.config = config
        self.gamestats = gamestats
        self._vol = self.gamestats.get_last_vol()
        self.min = config.volume["min_vol"]
        self.max = config.volume["max_vol"]
        self.increment = config.volume["increment"]
        self.vol = 0
        self.premutevol = self._vol
        self._clear = False
        self.set_volume(self._vol)
        self.with_button_handler = RUNNING_ON_PI
        if  self.with_button_handler:
            gpio = config.r_volumebutton["gpio"]
            increment_amount = config.r_volumebutton["increment"]
            self.encoder = rbh.ButtonHandler(gpio,
                                            increment_amount,
                                            callback=self.on_onoff)

        
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

        

    def remove_playlist(self): 
        subprocess.call("mpc rm  "
                        + self.config.sta_manager["playlist_name"], shell=True)           
        
    def stop_mpc(self): 
        subprocess.call("mpc stop ", shell=True)
        subprocess.call("mpc clear ", shell=True)
     
        

    def update(self):
        if self._clear:
            self.stop_mpc()
            self._clear = False
        if self.vol != self._vol:
            subprocess.call("mpc volume "+str(self._vol), shell=True)
            self.vol = self._vol


    def on_onoff(self, onoffv):
        pygame.event.post(pygame.event.Event(pygame.USEREVENT, 
                            name="_onoff", onoffv=onoffv))        
