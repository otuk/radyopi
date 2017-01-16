#!/usr/bin/python3

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

import os
#import signal
import threading
import subprocess
import sys

from RPi import GPIO
from queue import Queue

DEBUG = True

# SETTINGS
# ========

# The two pins that the encoder uses (BCM numbering).
GPIO_A = 26   
GPIO_B = 19

# The pin that the knob's button is hooked up to. If you have no button, set
# this to None.
GPIO_BUTTON = 13   # todo assign 


# the r.encoder has 96 (4x24) dents in 1 full rotation
# for each click lets in change by INCREMENT amount
INCREMENT = 2

# (END SETTINGS)
# 


# When the knob is turned, the callback happens in a separate thread. If
# those turn callbacks fire erratically or out of order, we'll get confused
# about which direction the knob is being turned, so we'll use a queue to
# enforce FIFO. The callback will push onto a queue, and all the actual
# volume-changing will happen in the main thread.
QUEUE = Queue()

# When we put something in the queue, we'll use an event to signal to the
# main thread that there's something in there. Then the main thread will
# process the queue and reset the event. If the knob is turned very quickly,
# this event loop will fall behind, but that's OK because it consumes the
# queue completely each time through the loop, so it's guaranteed to catch up.
#EVENT = threading.Event()

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
  
  def __init__(self, gpioA, gpioB, callback=None, buttonPin=None, buttonCallback=None):
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
      
    # Debounce.
    if channel == self.lastGpio:
      return
    
    # When both inputs are at 1, we'll fire a callback. If A was the most
    # recent pin set high, it'll be forward, and if B was the most recent pin
    # set high, it'll be reverse.
    self.lastGpio = channel
    if channel == self.gpioA and level == 1:
      if self.levB == 1:
        self.callback(INCREMENT)
    elif channel == self.gpioB and level == 1:
      if self.levA == 1:
        self.callback(-1*INCREMENT)


"""
if __name__ == "__main__":
  
  gpioA = GPIO_A
  gpioB = GPIO_B
  gpioButton = GPIO_BUTTON
  
  def on_press(value):
    # TODO what will the press do?
    #v.toggle()
    #print("Toggled mute to: {}".format(v.is_muted))
    EVENT.set()
  
  # This callback runs in the background thread. All it does is put turn
  # events into a queue and flag the main thread to process them. The
  # queueing ensures that we won't miss anything if the knob is turned
  # extremely quickly.
  def on_turn(delta):
    QUEUE.put(delta)
    EVENT.set()
    
  def consume_queue():
    while not QUEUE.empty():
      delta = QUEUE.get()
      handle_delta(delta)
      
  def handle_delta(delta):
    #if v.is_muted:
    #  debug("Unmuting")
    #  v.toggle()
    if delta == 1:
      #TODO  move right
      #vol = v.up()
      pass
    else:
      #TODO move left
      #vol = v.down()
      pass
    #print("Set volume to: {}".format(vol))

    
  #TODO what to do with this?  end of radyo on?  
  def on_exit(a, b):
    print("Exiting...")
    encoder.destroy()
    #TODO what to do with this?  end of radyo on?   no sys exit...
    sys.exit(0)
    
  debug("Volume knob using pins {} and {}".format(gpioA, gpioB))
  
  if gpioButton != None:
    debug("Volume button using pin {}".format(gpioButton))
  
  #debug("Initial volume: {}".format(v.volume))

  encoder = RotaryEncoder(GPIO_A, GPIO_B, callback=on_turn, buttonPin=GPIO_BUTTON, buttonCallback=on_press)
  signal.signal(signal.SIGINT, on_exit)
  
  while True:
    # This is the best way I could come up with to ensure that this script
    # runs indefinitely without wasting CPU by polling. The main thread will
    # block quietly while waiting for the event to get flagged. When the knob
    # is turned we're able to respond immediately, but when it's not being
    # turned we're not looping at all.
    # 
    # The 1200-second (20 minute) timeout is a hack; for some reason, if I
    # don't specify a timeout, I'm unable to get the SIGINT handler above to
    # work properly. But if there is a timeout set, even if it's a very long
    # timeout, then Ctrl-C works as intended. No idea why.
    EVENT.wait(1200)
    consume_queue()
    EVENT.clear()


"""
