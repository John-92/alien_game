# -*- coding=utf-8 -*-
# @Time: 2022/7/12 23:22
# @Author: John
# @File: settings.py
# @Software: PyCharm
class Settings():
    def __init__(self):
        self.screen_width=1200
        self.screen_height=650
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=1
        self.bullet_width=1200
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullets_allow=3

        self.alien_speed_factor=0.3
        self.fleet_drop_speed=10
        self.fleet_direction=1

        self.ship_limit = 3
