# -*- coding: utf-8 -*-

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
            "width" : 80,
            "height" : 80
        }

        self.dial = {
            "image" : "reddial.png",
            "width" : 4,
            "height" : 240
        }

        self.glasspanel = {
            "image" : "glasspanel.png",
            "width" : 340,
            "height" : 246,
            "x_shift" : -8,
            "y_shift" : -4
        }

        self.sta_display = {
            "width" : 100,
            "height" : 60,
            "inactive_color" : (190, 190, 190),
            "active_color" : (30, 30, 30),
            "font" : "monospace",
            "font_size" : 15, 
            "gap_x" : 20,
            "gap_y" : 13
        }

        self.sta_manager = {
            "rows" : 3,
            "playlist_name" : "radiopilist",
            
        }

        self.stations = [
            {
                "name" : "BBC Radio 1",
                "url"  : "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p",  
                "type" : "Pop Music",
                "region" : "Europe",
            },
            {
                "name" : "BBC Radio 2",
                "url"  : "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio2_mf_p",
                "type" : "Pop Music",
                "region" : "Europe",
            },
            {
                "name" : "BBC Radio 3",
                "url"  : "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio3_mf_p",
                "type" : "Orchestral Music",
                "region" : "Europe",
            },
            {
                "name" : "BBC Radio 4FM",
                "url"  : "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio4fm_mf_p",
                "type" : "News",
                "region" : "Europe",
            },
            {
                "name" : "BBC Radio 5LIVE",
                "url"  : "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio5live_mf_p",
                "type" : "News",
                "region" : "Europe",
            },
            {
                "name" : "BBC World Service",
                "url"  : "http://bbcwssc.ic.llnwd.net/stream/bbcwssc_mp1_ws-einws",
                "type" : "News",
                "region" : "Europe",
            },
            {
                "name" : "Radio Okapi",
                "url"  : "http://rs1.radiostreamer.com:8000/",
                "type" : "Ethnic Music",
                "region" : "Africa - DRC",
            },
            {
                "name" : "GLT News & Ideas",
                "url"  : "http://wgltradio.ilstu.edu:8000/wgltmain.mp3",
                "type" : "Pop Music",
                "region" : "North America",
            },
            {
                "name" : "Latvijas Radio 3 Klasika",
                "url"  : "http://lr3mp0.latvijasradio.lv:8004/",
                "type" : "Orchestral Music",
                "region" : "Europa",
            },

        ]

        
        self.levels =[
            {
                "name":"radyostart",
                "duration" : 8,
                "image":"yellowbg2.jpg",                
            },
            {
                "name":"lvl_1",
                "image":"radyoon.jpg",
            },
            {
                "name":"radyoend",
                "duration" : 3,
                "image" : "radyoend.jpg"
            }
        ]



        self.stats ={

        }
        
        
        
        



        
        
        
