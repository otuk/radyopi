# -*- coding: utf-8 -*-

"""
A pi internet radio that specializes in emulating
old analog radio behavior with the dial used to tune
to different stations.

Add any stations to  stationlist.py file under stations as per examples there.

Uses adafruit's pi 2.8 inch tft screen that is added as a hat to 40 gpio pins on pi
Also utilizes adafruits rotary encoder
And a potentimeter for volume and on/off options

It was built using pi2 with headless jessie installation
(pi b+, p2, pi 3 shd all be ok)
as it uses pygame/framebuffer drivers it does not need any xwindows 

During development press Q on keyboard to quit the application
Arrow keys to change station and volume without the need for the gpio hardware

"""


import os
import pygame

import settings
import radyopicontroller


def initialize_display():
    FBPATH = "/dev/fb1" # needed for adafruit tft screen to work with framebuffer
    if os.path.exists(FBPATH):
        os.environ["SDL_FBDEV"] = FBPATH

    disp_no = os.getenv('DISPLAY')
    if disp_no:
        #print("I'm running under X display = {0}".format(disp_no))
        pygame.display.init()
    else:
        #print(" display is not set")
        drivers = ['directfb', 'fbcon', 'svgalib']
        found = False
        for driver in drivers:
            if not os.getenv('SDL_VIDEODRIVER'):
                os.putenv('SDL_VIDEODRIVER', driver)
                try:
                    pygame.display.init()
                except pygame.error:
                    print("Driver: {0} failed".format(driver))
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
    while control.is_ON():
        control.handle_prelevel()
        while control.is_level_ON():
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
    
