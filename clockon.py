
import pygame

import common as c

import clock
import volumemanager


def pre(control):
    # check if the ON button is on  #TODO
    # if it is skip to radyoon

    if control.clk == None:
        #create data for display
        control.clk = clock.Clock(control.config)
        control.cg = pygame.sprite.Group()
        control.cg.add (control.clk)
        #c.debug(" clcok first time  initialized")
    control.gs.set_level_on();        


        
def evh(control):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            control.gs.set_exit_requested()
            control.gs.set_level_off()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                #simulate button action
                control.volman.on_onoff(1)
            elif event.key == pygame.K_q:
                control.gs.set_exit_requested()
                control.gs.set_level_off()
        elif event.type == pygame.USEREVENT:
            if event.name == "_onoff":
                status = event.onoffv
                c.debug("con compare status", status, control.gs.curr_state )
                if status != control.gs.curr_state :
                    control.gs.set_level_off()
                    

                    
def upd(control):
    control.cg.update()


    
def drw(control, screen):
    control.cg.draw(screen)

    
        
def pst(control):
    if control.gs.exit_requested:
        control.gs.curr_state = control.RADYOEND
        return
    else:       
        control.gs.curr_state = control.RADYOON


