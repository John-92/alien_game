# -*- coding=utf-8 -*-
# @Time: 2022/7/16 13:12
# @Author: John
# @File: game_stats.py
# @Software: PyCharm
class GameStats():
    def __init__(self,ai_settings):
        self.ai_settings=ai_settings
        self.reset_stats()

    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_limit