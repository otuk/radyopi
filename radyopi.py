# -*- coding: utf-8 -*-

import os
import pygame

import settings
import radyopicontroller


def initialize_display():
    FBPATH = "/dev/fb1"
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
    size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

    
    

def main():
    initialize_display()
    config = settings.Settings()
    control = radyopicontroller.Controller(config)
    control.set_icontitle()
    fps = pygame.time.Clock()
    
    screen = pygame.display.set_mode((config.width, config.height), pygame.FULLSCREEN)
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
    
