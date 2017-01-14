
class Stats:

    def __init__(self, config):
        self.game_on = False
        self.level_on = False
        self.curr_state = 0
        
    def set_game_off(self):
        self.game_on = False

    def set_level_off(self):
        self.level_on = False

    def set_game_on(self):
        self.game_on = True

    def set_level_on(self):
        self.level_on = True
        
