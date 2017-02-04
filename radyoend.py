
import pygame

import common as c



def pre(control):
    " this level is just to clear resources"
    control.gs.set_level_on();

        
        
def evh(control):
    control.gs.set_game_off()
    control.gs.set_level_off();            

                    
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
    c.warn("radyo end executed")
    control.volman.destroy()
    # release GPIO
    control.volman.clear_gpio()




