# -*- coding: utf-8 -*-

import stationlist

class Settings:
    
    def __init__(self):
        self.icon = "radio.png"
        self.title = "Radyo Pi"
        self.width = 320
        self.height = 240
        self.FPS = 30

        self.wifistatus = {
            "image_wifion" : "wifi_on.png",
            "image_wifioff" : "wifi_off.png",
            "width" : self.width//4,
            "height" : self.width//4
        }

        self.dial = {
            "image" : "reddial.png",
            "width" : self.width // 80,
            "height" : self.height
        }

        self.volume = {
            "min_vol" : 64,
            "max_vol" : 100,
            "ini_vol" : 73,
            "increment" : 3 
        }

        self.rencoder = {
            "gpioA" : 26,
            "gpioB" : 19,
            "gpioButton" : 13, # TODO
            "increment" : 2 
        }

        self.glasspanel = {
            "image" : "glasspanel.png",
            "width" : self.width + self.width // 10,
            "height" : self.height + self.height // 40,
            "x_shift" : -8,
            "y_shift" : -4
        }

        self.clock = {
            "width" : int(self.width //1.5) ,
            "height" : int(self.height // 2),
            "image" : "clockback2.png",
            "color" : (190, 190, 190),
            "font" : "Helvetica",
            "font_size_L" : 75,
            "font_size_M" : 30,
            "font_size_S" : 15, 
            "gap_y" : self.height // 20
        }
        
        self.sta_display = {
            "width" : self.width // 3.2,
            "height" : self.height // 4,
            "inactive_color" : (190, 190, 190),
            "active_color" : (30, 30, 30),
            "font" : "monospace",
            "font_size" : 15, 
            "gap_x" : self.width // 16,
            "gap_y" : self.height // 20
        }

        self.sta_manager = {
            "rows" : 3,
            "playlist_name" : "radiopilist",
            
        }

        self.stations = stationlist.stations
        
        self.levels =[
            {
                "name":"radyostart",
                "image":"yellowbg3.png",                
            },
            {
                "name":"radyoon",
                "image":"yellowbg3.png",                
            },
            {
                "name":"radyoend",
                "image" : "clockback2.png"
            }
        ]



        
        
        
        



        
        
        
