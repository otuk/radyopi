import pygame


def pre(control):
    control.gs.set_level_on()
    control.volman.set_volume(75)
    #print("radyo on PRE finished")
        
        
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
                control.volman.lower_volume(5)
            elif event.key == pygame.K_UP:
                control.volman.increase_volume(5)
            if event.key == pygame.K_q:
                control.volman.mute()
                control.volman.clear()
                control.gs.set_level_off()
                control.gs.set_game_off()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                pass
    d = control.dial.consume_queue()
    if d :
        control.staman.add_delta(d*-8)
        control.dial.add_delta(d*3)                        

            
                
def upd(control):
    control.vg.update()
    control.ig.update()    
    control.stag.update()    
    control.dg.update()

        
        
def drw(control, screen):
    #print("radyo on drawing")
    control.bdg.draw(screen)
    control.stag.draw(screen)
    control.ig.draw(screen)
    control.dg.draw(screen)
    control.gg.draw(screen)
    #print("radyo on drew")



def pst(control):
    pass


