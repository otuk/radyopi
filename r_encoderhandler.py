# -*- coding: utf-8 -*-

""""
A rotary encoder turns infinitely in either direction.
Turning it to the right will generate positive signal
Turning it to the left will generate negative signal
The adafruit rotary encoder I am using also has a button
that can  be pressed like a momentary ON/OFF switch.

The r.encoder uses 2 GPIO pins, 1 pin is for ground. 
The button we can just treat like an ordinary button.
Rather than poll constantly, we use threads and interrupts to listen on all three pins in one script.

This code heavily uses/borrows/modifies code from:
https://gist.github.com/savetheclocktower/9b5f67c20f6c04e65ed88f2e594d43c1#file-monitor-volume

"""

from RPi import GPIO
from queue import Queue

DEBUG = True


# When the knob is turned, the callback happens in a separate thread. If
# those turn callbacks fire erratically or out of order, we'll get confused
# about which direction the knob is being turned, so we'll use a queue to
# enforce FIFO. The callback will push onto a queue, and all the actual
# volume-changing will happen in the main thread.
QUEUE = Queue()


def debug(str):
  if not DEBUG:
    return
  print(str)

  
class RotaryEncoder:
  """
  A class to decode mechanical rotary encoder pulses.

  Ported to RPi.GPIO from the pigpio sample here: 
  http://abyz.co.uk/rpi/pigpio/examples.html
  """
  
  def __init__(self, gpioA, gpioB, increment,
               callback=None, buttonPin=None, buttonCallback=None):
    """
    Instantiate the class. Takes three arguments: the two pin numbers to
    which the rotary encoder is connected, plus a callback to run when the
    switch is turned.
    
    The callback receives one argument: a `delta` that will be either 1 or -1.
    One of them means that the dial is being turned to the right; the other
    means that the dial is being turned to the left. 

    """
    self.lastGpio = None
    self.gpioA    = gpioA
    self.gpioB    = gpioB
    self.increment = increment
    self.neg_increment = -1*self.increment
    self.callback = callback
    debug("callback set"+str(self.callback))
    
    self.gpioButton     = buttonPin
    self.buttonCallback = buttonCallback
    
    self.levA = 0
    self.levB = 0
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.gpioA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(self.gpioB, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    GPIO.add_event_detect(self.gpioA, GPIO.BOTH, self._callback)
    GPIO.add_event_detect(self.gpioB, GPIO.BOTH, self._callback)
    
    if self.gpioButton:
      GPIO.setup(self.gpioButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
      GPIO.add_event_detect(self.gpioButton, GPIO.FALLING, self._buttonCallback, bouncetime=500)


      
    
  def destroy(self):
    debug("destroying rencoder handler")
    GPIO.remove_event_detect(self.gpioA)
    GPIO.remove_event_detect(self.gpioB)
    GPIO.cleanup()


    
    
  def _buttonCallback(self, channel):
    self.buttonCallback(GPIO.input(channel))

    

    
  def _callback(self, channel):
    level = GPIO.input(channel)
    if channel == self.gpioA:
      self.levA = level
    else:
      self.levB = level
      
    # De-bounce.
    if channel == self.lastGpio:
      return
    
    # When both inputs are at 1, we'll fire a callback. If A was the most
    # recent pin set high, it'll be forward, and if B was the most recent pin
    # set high, it'll be reverse.
    self.lastGpio = channel
    if channel == self.gpioA and level == 1:
      if self.levB == 1:
        self.callback(self.increment)
    elif channel == self.gpioB and level == 1:
      if self.levA == 1:
        self.callback(self.neg_increment)


