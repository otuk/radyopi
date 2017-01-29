
import pygame

import stats
import radyostart
import clockon
import radyoon
import radyoend
import background
import wifistatus
import glasspanel



class Controller:

    PRE = 0
    EVH = 1
    UPD = 2
    DRW = 3
    PST = 4

    
    def __init__(self, config):
        # all the settings are here
        self.config = config
        # current state is in gs(gamestate) object
        self.gs = stats.Stats(config)
        # background for the station dial
        self.backdial = background.Background(config, self.gs)
        self.bdg = pygame.sprite.Group()
        self.bdg.add(self.backdial)
        # wifi checker
        # TODO call the wifi checker during radyo on? perf impact?
        self.wifis = wifistatus.Wifistatus(config, self.gs)
        self.wfg = pygame.sprite.Group()
        self.wfg.add(self.wifis)
        # transparent glass over the dial
        self.glass = glasspanel.Glasspanel(config, self.gs)
        self.gg = pygame.sprite.Group()
        self.gg.add(self.glass)
        # additionally each level creates their own needed elements
        # and populate the controller
        
        
    
    def screen_ready(self, screen):
        self.screen = screen
        self.gs.game_on = True

        
    def is_ON(self):
        return self.gs.game_on

    
    def is_level_ON(self):
        return self.gs.level_on

    
    def handle_prelevel(self):
        Controller.levels[self.gs.curr_state][Controller.PRE](self)
    
    def event_handler(self):
        Controller.levels[self.gs.curr_state][Controller.EVH](self)

    def update(self):
        Controller.levels[self.gs.curr_state][Controller.UPD](self)

    def draw(self, screen):
        Controller.levels[self.gs.curr_state][Controller.DRW](self, screen)

    def handle_postlevel(self):
        Controller.levels[self.gs.curr_state][Controller.PST](self)
        


    levels = [
        [radyostart.pre, radyostart.evh, radyostart.upd, radyostart.drw, radyostart.pst],
        [clockon.pre, clockon.evh, clockon.upd, clockon.drw, clockon.pst],
        [radyoon.pre, radyoon.evh, radyoon.upd, radyoon.drw, radyoon.pst],
        [radyoend.pre, radyoend.evh, radyoend.upd, radyoend.drw, radyoend.pst],
    ]
        
