
import pygame

import common as c
import volumemanager
import dial


def pre(control):
    control.gs.set_level_on()
    
        
def evh(control):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            control.gs.set_exit_requested()
            control.gs.set_level_off()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                control.gs.set_level_off()
            if event.key == pygame.K_q:
                control.gs.set_exit_requested()
                control.gs.set_level_off()
                

                
def upd(control):
    if control.wifis.check_internet_access() :
        control.gs.set_level_off()
        print ( "wifi ON,  moving to next level")
    else:
        print ( "wifi no good will try more")
        pass
    control.gs.set_level_off()  # TODO TEST only for nointernet connection/TEST

    
def drw(control, screen):  #TODO show what wifi is being tried on screen
    control.bdg.draw(screen)
    control.wfg.draw(screen)
    control.gg.draw(screen)
    

    
def pst(control):
    if control.gs.exit_requested:
          control.gs.curr_state = control.RADYOEND
          return      
    #create the long living objects
    # start the volume manager
    control.volman = volumemanager.VolumeManager(control.config, control.gs)
    control.vg = pygame.sprite.Group()
    control.vg.add(control.volman)
    #add the dial manager
    control.dial = dial.Dial(control.config, control.gs)
    control.dg = pygame.sprite.Group()
    control.dg.add(control.dial)
    control.gs.curr_state = control.CLOCKON
    c.debug( "-- radyostart POST executed gs state is "+str(control.gs.curr_state) )
