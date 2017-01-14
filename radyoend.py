
import pygame
    
def pre(control):
    image = pygame.image.load(control.config.levels[control.gs.curr_state]["image"])
    image = pygame.transform.scale(image,(control.config.width, control.config.height))
    control.screen.blit(image, (0,0))
    control.gs.set_level_on();

        
        
def evh(control):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            control.gs.set_game_off()
            control.gs.set_level_off()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                control.gs.curr_state = 1
                control.gs.reset_life()
                control.gs.set_level_off();
            elif event.key == pygame.K_q:
                control.gs.set_level_off()
                control.gs.set_game_off()


                    
def upd(control):
    pass


    
def drw(control, screen):
    pass

    
        
def pst(control):
    pass

