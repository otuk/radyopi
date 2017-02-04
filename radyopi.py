#! /usr/bin/env python3

"""
A pi internet radio that emulates old analog radio feel.
On off button and a a rotary dial is used just as in an
old analog radio. The red colorred dial indicator used to show
what station is tuned into.

Add any stations to  stationlist.py file under stations as per examples there.

Uses adafruit's pi 2.8 inch tft screen that is added as a hat to 40 gpio pins on pi
Also utilizes adafruits rotary encoder.
And an audio potentimeter for volume and on/off control.

It was built using pi2 with headless jessie installation.
It uses pygame/framebuffer drivers it does not need any xwindows.
(pi b+, p2, pi 3 shd all be ok)

During development press Q on keyboard to quit the application.
F-key to switch between clock (OFF) and radyo (ON) views.
Left/Right-Arrow keys to change station and Up/Down Arrow keys to adjust volume without the need for the gpio hardware

"""

import os
import pygame

import common as c
import settings
import radyopicontroller


def initialize_display():
    FBPATH = "/dev/fb1" # needed for adafruit tft screen to work with framebuffer
    if os.path.exists(FBPATH):
        os.environ["SDL_FBDEV"] = FBPATH
    disp_no = os.getenv('DISPLAY')
    if disp_no:
        c.debug("I'm running under X display = {0}".format(disp_no))
        pygame.display.init()
    else:
        c.debug(" display is not set")
        drivers = ['directfb', 'fbcon', 'svgalib']
        found = False
        for driver in drivers:
            if not os.getenv('SDL_VIDEODRIVER'):
                os.putenv('SDL_VIDEODRIVER', driver)
                try:
                    pygame.display.init()
                except pygame.error:
                    c.error("Driver: {0} failed".format(driver))
                    continue
                found = True
                break
    
        if not found:
            raise Exception('No suitable video driver found!')
    pygame.mouse.set_visible(False)
    pygame.font.init()

    
    

def main():
    config = settings.Settings()
    initialize_display()
    size = (config.width, config.height)
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    control = radyopicontroller.Controller(config)
    fps = pygame.time.Clock()
    
    control.screen_ready(screen)

    """ main loop """
    while control.is_game_on():
        control.handle_prelevel()
        while control.is_level_on():
            control.event_handler()
            control.update()
            control.draw(screen)
            pygame.display.update()
            fps.tick(config.FPS)
        control.handle_postlevel()
    """" end of main loop """

    """ clean exit """
    pygame.quit()


    
        
if __name__ == "__main__":
    main()
    
