# -*- coding: utf-8 -*-

import pygame
import importlib

mRPi = importlib.find_loader("RPi")
RUNNING_ON_PI = mRPi is not None
if RUNNING_ON_PI:
    import r_encoderhandler as reh



class Dial(pygame.sprite.Sprite):
    
    def __init__(self, config, gs):
        super().__init__()
        self.gs = gs
        self.image = pygame.image.load(config.dial["image"])
        self.image = pygame.transform.scale(self.image,(config.dial["width"],
                                                        config.dial["height"]))
        self.rect = self.image.get_rect()
        self.delta = 0
        self._x =  config.width // 2
        self._y = 0
        self.rect.x = self._x + self.delta
        self.rect.y = self._y
        self.with_encoder = RUNNING_ON_PI
        if  self.with_encoder:
            gpioA = config.rencoder["gpioA"]
            gpioB = config.rencoder["gpioB"]
            gpioButton = config.rencoder["gpioButton"]
            increment_amount = config.rencoder["increment"]
            self.encoder = reh.RotaryEncoder(gpioA,
                                             gpioB,
                                             increment_amount,
                                             callback=self.on_turn,
                                             buttonPin=gpioButton,
                                             buttonCallback=self.on_press)
        print("dial created with encoder", gpioA, gpioB, gpioButton)

        

    def add_delta(self, d):
        self.delta += d

        
        
    def update(self):
        # the following is to emulate analog
        # dial movement and nothing else
        if self.rect.x < self._x:
            self.delta += 1
        elif self.rect.x > self._x:
            self.delta += -1
       # this is the real update for dial     
        self.rect.x = self._x + self.delta


        
    def on_press(self, value):
        #TODO what happens when the user presses the push button?
        pass 


    
    # This callback runs in the background thread. All it does is put turn
    # events into pygame event queue 
    def on_turn(self, delta):
        #print("on turn + delta ", delta)
        pygame.event.post(pygame.event.Event(pygame.USEREVENT,
                                             name="_dial", side=delta))



    def destroy(self):
        if self.with_encoder:
            self.encoder.destroy()
