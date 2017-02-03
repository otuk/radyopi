# -*- coding: utf-8 -*-

"""

The button  uses 1 GPIO pins & the other physical connection is for ground. 
Rather than poll constantly, the button will be watched for gpio  events.
This code heavily uses/borrows/modifies code from:
https://gist.github.com/savetheclocktower/9b5f67c20f6c04e65ed88f2e594d43c1#file-monitor-volume

"""

from RPi import GPIO

DEBUG = True

def debug(str):
  if not DEBUG:
    return
  print(str)

BS_ON = 1
BS_OFF = 0
  
class ButtonHandler:
  """
  A class that watches for button sttate changes

  """
  
  def __init__(self, buttonPin=None, buttonCallback=None):
    """
    Instantiate the class. Takes 2 arguments: the  pin number to
    monitor plus a callback to run when the state is changed
    
    The callback receives one argument: a `delta` that will be either BS_ON or BS_OFF.
    One of them means that the button state is off,  the other
    means that the button is on.
    """

    self.gpioButton     = buttonPin
    self.buttonCallback = buttonCallback
    self.level = BS_OFF

    GPIO.setmode(GPIO.BCM)
    if self.gpioButton:
      GPIO.setup(self.gpioButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
      GPIO.add_event_detect(self.gpioButton, GPIO.BOTH,  self._buttonCallback, bouncetime=500)
      self.buttonCallback(self.level)

    
  def _buttonCallback(self, channel):
    self.level = GPIO.input(channel)
    print("button calling back ", self.level)
    self.buttonCallback(self.level)



  def destroy(self):
    debug("destroying button handler")
    GPIO.remove_event_detect(self.gpioButton)
