#

"""

The button  uses 2 GPIO pins & the other physical connection is for ground. 
The idea is to read analog volume levels from the potentiometer without an ADC
(because I dont have a MPC3008 handy)

"""

from RPi import GPIO

import common as c
import time


GPIO.setmode(GPIO.BCM)

a_pin = 20 
b_pin = 21

def discharge():
  GPIO.setup(a_pin, GPIO.IN)
  GPIO.setup(b_pin, GPIO.OUT)
  GPIO.output(b_pin, False)
  time.sleep(0.045)

def charge_time():
  GPIO.setup(b_pin, GPIO.IN)
  GPIO.setup(a_pin, GPIO.OUT)
  count = 0
  GPIO.output(a_pin, True)
  while not GPIO.input(b_pin):
    count = count + 1
  return count

def analog_read():
  discharge()
  return charge_time()

while True:
  print(analog_read())
  time.sleep(.1)




  
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


    
  def _buttonCallback(self, channel):
    self.level = GPIO.input(channel)
    c.debug("button calling back ", self.level)
    self.buttonCallback(self.level)



  def destroy(self):
    c.debug("destroying button handler")
    GPIO.remove_event_detect(self.gpioButton)
