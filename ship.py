# -*- coding=utf-8 -*-
# @Time: 2022/7/12 23:29
# @Author: John
# @File: ship.py
# @Software: PyCharm
import pygame
class Ship():
    def __init__(self,ai_settings,screen):
        self.screen=screen
        self.ai_settings=ai_settings
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.center=float(self.rect.centerx)


        self.moving_right=False
        self.moving_left=False

    def update(self):
        if self.moving_right and self.rect.right< self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            # self.rect.centerx-=1.5
            self.center-=self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        # print("rect.centerx"+str(self.center)+str(self.rect.centerx))


    def blitme(self):
        self.screen.blit(self.image,self.rect)

