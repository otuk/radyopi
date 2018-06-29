# -*- coding: utf-8 -*-


import subprocess

import station

class StationManager():

    def __init__(self, config, gs, ig):
        super().__init__()
        self.config = config
        self.gs = gs
        self.activesta = None
        self.delta = self.gs.get_last_delta()
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
        print("will write playlist")
        self.writeplaylist()
        self.set_delta(self.delta)

        
    def writeplaylist(self):
        print("will clear")
        subprocess.call("mpc -w clear ", shell=True)
        print("cleared")
        subprocess.call("mpc -w rm " + self.playlistname, shell=True)
        subprocess.call("mpc -w save " + self.playlistname, shell=True)
        for sta in self.stas:
            url = sta.url
            print("adding")
            subprocess.call("mpc add " + url, shell=True)
        subprocess.call("mpc -w save " + self.playlistname, shell=True)
        print("loading")
        subprocess.call("mpc load " + self.playlistname, shell=True)
                
        
    def add_delta(self, d):
        self.delta += d
        for sta in self.stas:
            sta.set_delta(self.delta)

            
    def set_delta(self,d):
        self.delta = d
        for sta in self.stas:
            sta.set_delta(self.delta)

            
