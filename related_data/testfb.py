import os
import pygame

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
                c.debug("Driver: {0} failed".format(driver))
                continue
            found = True
            break
    
        if not found:
            raise Exception('No suitable video driver found!')




    
size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
