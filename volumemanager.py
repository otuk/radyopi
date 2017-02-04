# -*- coding: utf-8 -*-
  

import subprocess
import pygame

import common as c

if c.RUNNING_ON_PI:
    import r_buttonhandler as rbh



class VolumeManager(pygame.sprite.Sprite):

    
    def __init__(self, config, gamestats):
        super().__init__()
        self.config = config
        self.gamestats = gamestats
        self.reset_volume()
        self.min = config.volume["min_vol"]
        self.max = config.volume["max_vol"]
        self.increment = config.volume["increment"]
        self.vol = 0
        self.premutevol = self._vol
        self._clear = False
        self.set_volume(self._vol)
        self.with_button_handler = c.RUNNING_ON_PI
        if  self.with_button_handler:
            gpio = config.r_volumebutton["gpio"]
            c.debug("vol bu" , gpio)
            #increment_amount = config.r_volumebutton["increment"] # TODO
            self.onoffbutton = rbh.ButtonHandler(buttonPin=gpio,
                                            buttonCallback=self.on_onoff)
            self.on_onoff(self.onoffbutton.level)
            
        
    def set_volume(self, v):
        if v > self.max:
            self._vol = self.max
        elif self._vol < self.min:
            self._vol = self.min
        else :
            self._vol = v

            
    def reset_volume(self):
        self._vol = self.gamestats.get_last_vol()        
            
            
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
        #c.debug("on off generating event")
        if onoffv == 0:
            onoffv = 1
        else:
            onoffv = 2
        pygame.event.post(pygame.event.Event(pygame.USEREVENT, 
                            name="_onoff", onoffv=onoffv))        



    def destroy(self):
        if self.with_button_handler:
            self.onoffbutton.destroy()

        
    def clear_gpio(self):
        if self.with_button_handler:
            GPIO.cleanup()
