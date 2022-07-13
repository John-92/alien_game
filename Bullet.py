# -*- coding=utf-8 -*-
# @Time: 2022/7/13 23:08
# @Author: John
# @File: Bullet.py
# @Software: PyCharm
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super(Bullet, self).__init__()
        self.screen=screen
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        self.y=float(self.rect.y)

        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

        # self.bullets_allowed=3


    def update(self):
        self.y -=self.speed_factor
        self.rect.y=self.y


    def draw_bullet(self):
        #def rect(surface, color, rect): # real signature unknown; restored from __doc__
        pygame.draw.rect(self.screen,self.color,self.rect)