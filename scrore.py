# -*- coding=utf-8 -*-
# @Time: 2022/7/17 16:41
# @Author: John
# @File: scrore.py
# @Software: PyCharm
import pygame.font


class Scoreboard:
    def __init__(self,ai_settings,screen,stats):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings
        self.stats=stats

        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)

        self.pre_score()

 #将分数转化为pygame文字对象
    def pre_score(self):
        # score_str=str(self.stats.score)
        rounded_score=int(round(self.stats.score,-1))
        print("rounede_score"+str(rounded_score))
        score_str="{:,}".format(rounded_score)
        self.score_iamge=self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)

        self.score_rect=self.score_iamge.get_rect()
        self.score_rect.right=self.screen_rect.width-20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_iamge,self.score_rect)



