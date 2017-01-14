
import pygame

import stats
import radyostart
import radyoend
import radyoon
import background
import wifistatus
import dial
import glasspanel
import station
import stationmanager
import volumemanager



class Controller:

    PRE = 0
    EVH = 1
    UPD = 2
    DRW = 3
    PST = 4

    
    def __init__(self, config):
        self.config = config
        self.gs = stats.Stats(config)
        self.backdial = background.Background(config, self.gs)
        self.bdg = pygame.sprite.Group()
        self.bdg.add(self.backdial)
        self.wifis = wifistatus.Wifistatus(config, self.gs)
        self.wfg = pygame.sprite.Group()
        self.wfg.add(self.wifis)
        self.dial = dial.Dial(config, self.gs)
        self.dg = pygame.sprite.Group()
        self.dg.add(self.dial)
        self.glass = glasspanel.Glasspanel(config, self.gs)
        self.gg = pygame.sprite.Group()
        self.gg.add(self.glass)
        self.volman = volumemanager.VolumeManager(config)
        self.vg = pygame.sprite.Group()
        self.vg.add(self.volman)
        self.ig = pygame.sprite.Group()
        self.staman = stationmanager.StationManager(config, self.ig)
        self.stag = pygame.sprite.Group()
        for sta in self.staman.stas:
            self.stag.add(sta)
        
        
        
    def set_icontitle(self):
        # in full screen mode this needs to go away
        icon = pygame.image.load(self.config.icon)
        pygame.display.set_icon(icon)
        pygame.display.set_caption(self.config.title)
        return icon
    
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
        [radyoon.pre, radyoon.evh, radyoon.upd, radyoon.drw, radyoon.pst],
        [radyoend.pre, radyoend.evh, radyoend.upd, radyoend.drw, radyoend.pst]
    ]
        
