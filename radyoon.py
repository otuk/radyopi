# -*- coding: utf-8 -*-

import pygame


import volumemanager
import stationmanager
import dial



def pre(control):
    control.volman = volumemanager.VolumeManager(control.config)
    control.vg = pygame.sprite.Group()
    control.vg.add(control.volman)
    control.ig = pygame.sprite.Group()
    control.staman = stationmanager.StationManager(control.config, control.ig)
    control.stag = pygame.sprite.Group()
    for sta in control.staman.stas:
        control.stag.add(sta)
    control.dial = dial.Dial(control.config, control.gs)
    control.dg = pygame.sprite.Group()
    control.dg.add(control.dial)
    control.gs.set_level_on()
    
        

    
def evh(control):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            control.gs.set_game_off()
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
                control.gs.set_level_off()
                control.gs.set_game_off()
            if event.key == pygame.K_f:
                control.gs.set_level_off()
    # TODO the following polling can be made into a pygame user event
    # and can be part of event loop
    if control.dial.with_encoder:
        d = control.dial.consume_queue()
        if d != 0 :
            control.staman.add_delta(d*-8)
            control.dial.add_delta(d*3)                        

        
            
                
def upd(control):
    control.vg.update()
    control.ig.update()    
    control.stag.update()    
    control.dg.update()

        
        
def drw(control, screen):
    control.bdg.draw(screen)
    control.stag.draw(screen)
    control.ig.draw(screen)
    control.dg.draw(screen)
    control.gg.draw(screen)



def pst(control):
    # do some clean up
    # TODO  what else?
    control.dial.destroy()
    #turn off mpc
    control.volman.mute()    
    control.volman.kill_mpc()
    # radyo off mode
    control.gs.curr_state += 1 
