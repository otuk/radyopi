
import pygame

import clock



def pre(control):
    control.gs.set_level_on();

        
        
def evh(control):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            control.gs.set_game_off()
            control.gs.set_level_off()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                control.gs.set_level_off()
                control.gs.set_game_off()


                    
def upd(control):
    pass


    
def drw(control, screen):
    pass

    
        
def pst(control):
    #clean up GPIO 
    # this level is only to shutdown  and clean resources
    # TODO clean - all - GPIO
    control.dial.destroy()
    control.volman.mute()
    control.volman.stop_mpc()    # radyo off mode
    control.volman.remove_playlist()
    print("radyo end executed")
    control.volman.destroy()
    control.volman.clear_gpio()




