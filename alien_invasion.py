# import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("hello world")
    ship = Ship(ai_settings,screen)
    bullets=Group()
    # pygame.display.set_gamma(230,230,230)
    while True:
        #对函数调用
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()

        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,bullets)
run_game()