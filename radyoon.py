# -*- coding: utf-8 -*-

import pygame

import common as c

import stationmanager
import dial



def pre(control):
    control.ig = pygame.sprite.Group()
    control.staman = stationmanager.StationManager(control.config,
                                                       control.gs, control.ig)
    control.stag = pygame.sprite.Group()
    for sta in control.staman.stas:
        control.stag.add(sta)
    control.volman.reset_volume()
    control.gs.set_level_on()
    c.debug("radyo on pre executed")
    

    
def evh(control):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            control.gs.set_exit_requested()
            control.gs.set_level_off()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                control.staman.add_delta(5)
                control.dial.add_delta(-3)
            elif event.key == pygame.K_RIGHT:
                control.staman.add_delta(-5)
                control.dial.add_delta(3)                
            if event.key == pygame.K_DOWN:
                control.volman.lower_volume(control.volman.increment)
            elif event.key == pygame.K_UP:
                control.volman.increase_volume(control.volman.increment)
            if event.key == pygame.K_q:
                control.gs.set_exit_requested()
                control.gs.set_level_off()
            if event.key == pygame.K_f:
                #simulate button event
                control.volman.on_onoff(0)
        elif event.type == pygame.USEREVENT:
            if event.name == "_dial":
                d = event.side
                control.staman.add_delta(-3*d)
                control.dial.add_delta(2*d)
            elif event.name == "_onoff":
                status = event.onoffv
                c.debug("ron compare status", status, control.gs.curr_state)
                if status != control.gs.curr_state :
                    control.gs.set_level_off()
        
            
                
def upd(control):
    control.vg.update()
    control.stag.update()    
    control.ig.update()    
    control.dg.update()

        
        
def drw(control, screen):
    control.bdg.draw(screen)
    control.stag.draw(screen)
    control.ig.draw(screen)
    control.dg.draw(screen)
    control.gg.draw(screen)



def pst(control): 
    # turn off volume 
    control.gs.set_last_vol(control.volman.vol)
    control.gs.set_last_delta(control.staman.delta)
    #turn off mpc
    control.volman.mute()    
    control.volman.update()
    control.volman.stop_mpc()
    if control.gs.exit_requested:
        control.gs.curr_state = control.RADYOEND
        return
    control.gs.curr_state = control.CLOCKON # back to clock
