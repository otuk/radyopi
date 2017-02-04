import importlib

mRPi = importlib.find_loader("RPi")
RUNNING_ON_PI = mRPi is not None

DEBUG = True
WARN = True

def debug(*str):
  if not DEBUG:
      return
  print(*str)


def warn(*str):
  if not WARN:
      return      
  print(*str)


def error(*str):     
  print(*str)
