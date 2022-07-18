# -*- coding=utf-8 -*-
# @Time: 2022/7/17 15:03
# @Author: John
# @File: button.py
# @Software: PyCharm
import pygame.font


class Button():
    def __init__(self,screen,msg):
        self.screen=screen
        self.screen_rect=screen.get_rect()

        self.width,self.height=200,50
        self.button_color=(0,255,255)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)

        self.rect=pygame.Rect(0,0,self.width,self.height)
        #1、作为Rect的一个属性
        #2、用来将外部的参数转换为内部的参数，方便内部方法调用
        self.rect.center=self.screen_rect.center

        self.pre_msg(msg)


    def pre_msg(self,msg):
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center


    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)


