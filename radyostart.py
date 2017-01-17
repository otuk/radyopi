
import pygame


def pre(control):
    control.gs.set_level_on()
    
        
def evh(control):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            control.gs.set_game_off()
            control.gs.set_level_off()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                control.gs.set_level_off()
            if event.key == pygame.K_q:
                control.gs.set_level_off()
                control.gs.set_game_off()



                
def upd(control):
    if control.wifis.check_internet_access() :
        control.gs.set_level_off()
        #print ( "wifi ON,  moving to next level")
    else:
        #print ( "wifi no good will try more")
        pass
    control.gs.set_level_off()  # TODO TEST only for nointernet connection/TEST

    
def drw(control, screen):
    control.bdg.draw(screen)
    control.wfg.draw(screen)
    control.gg.draw(screen)
    

    
def pst(control):
    control.gs.curr_state += 1
    #print ( "-- radyostart POST executed gs state is ", control.gs.curr_state )
