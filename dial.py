# -*- coding: utf-8 -*-

import pygame

import r_encoderhandler as reh

#TODO ? is this needed?
gpioA = reh.GPIO_A
gpioB = reh.GPIO_B
gpioButton = reh.GPIO_BUTTON


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
        self.encoder = reh.RotaryEncoder(reh.GPIO_A,
                                         reh.GPIO_B,
                                         callback=self.on_turn,
                                         buttonPin=None,
                                         buttonCallback=self.on_press)
        print("dial created with encoder")

        

    def add_delta(self, d):
        self.delta += d

        
        
    def update(self):
        #reh.EVENT.wait(1200)
        #print("dial update called")
        #self.consume_queue()
        #reh.EVENT.clear()

        # the following is to emulate analog
        # dial movement and nothing else
        if self.rect.x < self._x:
            self.delta += 1
        elif self.rect.x > self._x:
            self.delta += -1
       # this is the real update for dial     
        self.rect.x = self._x + self.delta

        
    def on_press(self, value):
        # TODO what will the press do?
        #v.toggle()
        #print("Toggled mute to: {}".format(v.is_muted))
        #reh.EVENT.set()
        pass
  
    # This callback runs in the background thread. All it does is put turn
    # events into a queue and flag the main thread to process them. The
    # queueing ensures that we won't miss anything if the knob is turned
    # extremely quickly.
    def on_turn(self, delta):
        print("on turn + delta ", delta)
        reh.QUEUE.put(delta)
        #reh.EVENT.set()
    
    def consume_queue(self):
        d = 0
        while not reh.QUEUE.empty():
            print("found something in queue")
            delta = reh.QUEUE.get()
            d += delta
            print("delta is ", delta)
            #self.handle_delta(delta)
        return d     

"""            
    def handle_delta(self, delta):
        #if v.is_muted:
        #  debug("Unmuting")
        #  v.toggle()
        if delta == 1:
            #TODO  move right
            #vol = v.up()
            self.delta += delta*10
            #pass
        else:
            #TODO move left
            #vol = v.down()
            self.delta -= delta*10
        print("dial delat tota is", self.delta)    
            #pass
        #print("Set volume to: {}".format(vol))

"""
        
