
import pygame

import clock



def pre(control):
    #create data for display
    control.clk = clock.Clock(control.config)
    control.cg = pygame.sprite.Group()
    control.cg.add (control.clk)
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


                    
def upd(control):
    control.cg.update()


    
def drw(control, screen):
    control.cg.draw(screen)

    
        
def pst(control):
    #clean up first
    control.cg.remove()
    #set level to radyo on
    control.gs.curr_state = 2


