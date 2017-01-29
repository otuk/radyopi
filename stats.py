
class Stats:

    def __init__(self, config):
        self.game_on = False
        self.level_on = False
        self.curr_state = 0
        self.last_vol = config.volume["ini_vol"]
        self.last_delta = config.width // 2 

    def set_game_off(self):
        self.game_on = False

    def set_level_off(self):
        self.level_on = False

    def set_game_on(self):
        self.game_on = True

    def set_level_on(self):
        self.level_on = True
        
    def set_last_vol(self, v):
        self.last_vol = v

    def get_last_vol(self):
        return self.last_vol

    def set_last_delta(self, d):
        self.last_delta = d

    def get_last_delta(self):
        return self.last_delta
        
