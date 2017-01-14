# -*- coding: utf-8 -*-

import pygame
import socket

INITIAL_CHECK_INTERVAL = 1
FAILED_CHECK_INTERVAL = 10
SUCCESS_CHECK_INTERVAL = 120
CHECK_INTERVAL = FAILED_CHECK_INTERVAL

class Wifistatus(pygame.sprite.Sprite):
    
    def __init__(self, config, gs):
        super().__init__()
        self.config = config
        CHECK_INTERVAL = config.FPS * INITIAL_CHECK_INTERVAL
        self.wifion = False
        self.onimg = pygame.image.load(config.wifistatus["image_wifion"])
        self.offimg = pygame.image.load(config.wifistatus["image_wifioff"])
        self.set_image(self.offimg)
        self.rect = self.image.get_rect()
        self.rect.centerx = config.width // 2
        self.rect.centery = config.height // 2
        self.checkinterval = CHECK_INTERVAL



    def set_image(self, img):
        self.image = img
        self.image = pygame.transform.scale(self.image,
                                            (self.config.wifistatus["width"],
                                             self.config.wifistatus["height"]))
        
        
    def check_internet_access(self, host="8.8.8.8", port=53, timeout=3):
        """
        Host: 8.8.8.8 (google-public-dns-a.google.com)
        OpenPort: 53/tcp
        Service: domain (DNS/TCP)
        """
        if self.checkinterval == 0:
            pass
        else:
            self.checkinterval -= 1    
            return self.wifion

        print("checking wifi "+ str(self.checkinterval))

        
        try:
            socket.setdefaulttimeout(timeout)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.close()
            self.wifion = True
            self.set_image(self.onimg)
            self.checkinterval = self.config.FPS * SUCCESS_CHECK_INTERVAL - 1
            return True
        except Exception as ex:
            print("Problem connecting to internet")
            print(str(ex))
            self.wifion = False
            self.set_image(self.offimg)
            self.checkinterval = self.config.FPS * FAILED_CHECK_INTERVAL - 1
            return False
        
