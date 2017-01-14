# -*- coding: utf-8 -*-


import subprocess

import station

class StationManager():

    def __init__(self, config, ig):
        super().__init__()
        self.config = config
        self.activesta = None
        self.delta = 0
        self.stas = []
        s = 0
        self.rows = config.sta_manager["rows"]
        lastx = [0 for i in range(3)]
        lasti = 0
        
        for sta in self.config.stations:
            row = s % self.rows
            col = s // self.rows
            nsta = station.Station(config, s, col, row, lastx[row], lasti, ig)
            self.stas.append(nsta)
            lastx[row] = nsta.ends_at()
            lasti = nsta.iends_at()
            s += 1
        self.playlistname = config.sta_manager["playlist_name"]    
        self.writeplaylist()

        
    def writeplaylist(self):
        subprocess.call("mpc -w clear ", shell=True)
        subprocess.call("mpc -w rm " + self.playlistname, shell=True)
        for sta in self.stas:
            url = sta.url
            subprocess.call("mpc add " + url, shell=True)
        subprocess.call("mpc -w save " + self.playlistname, shell=True)
        subprocess.call("mpc load " + self.playlistname, shell=True)
                
        
    def add_delta(self, d):
        self.delta += d
        for sta in self.stas:
            sta.set_delta(self.delta)

            
    def set_delta(self,d):
        self.delta = d
        for sta in self.stas:
            sta.set_delta(self.delta)

        
