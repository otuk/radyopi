
import pygame

import clock
import volumemanager



def pre(control):
    # check if the ON button is on
    # if it is skip to radyoon
    if control.clk == None:
        #create data for display
        control.clk = clock.Clock(control.config)
        control.cg = pygame.sprite.Group()
        control.cg.add (control.clk)
        #print(" clcokon initialized")
    if control.volman == None:
        control.volman = volumemanager.VolumeManager(control.config, control.gs)
        control.vg = pygame.sprite.Group()
        control.vg.add(control.volman)
    control.gs.set_level_on();        
        
def evh(control):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            control.gs.set_game_off()
            control.gs.set_level_off()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                control.gs.set_level_off();
            elif event.key == pygame.K_q:
                control.gs.set_level_off()
                control.gs.set_game_off()
        elif event.type == pygame.USEREVENT:
            if event.name == "_onoff":
                status = event.onoffv
                print("con compare status", status, control.gs.curr_state )
                if status != control.gs.curr_state :
                    control.gs.set_level_off()
                    return
                    

                    
def upd(control):
    control.cg.update()


    
def drw(control, screen):
    control.cg.draw(screen)

    
        
def pst(control):
    #clean up first

    control.cg.empty()
    control.clk = None
    control.cg = None
    #print("clockon cleared")
    #set level to radyo on
    control.gs.curr_state = 2


