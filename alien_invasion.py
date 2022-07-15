import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("hello world")
    ship = Ship(ai_settings,screen)
    bullets=Group()
    aliens=Group()
    gf.create_fleet(ai_settings,screen,aliens)
    f = pygame.font.Font('C:/Windows/Fonts/simkai.ttf', 100)
    text = f.render("FUCK YOU", False, (100, 5, 255), (230, 230, 230))
    print(text)
    textRect = text.get_rect()
    textRect.center = (200, 200)

    alien=Alien(ai_settings,screen)

    # pygame.display.set_gamma(230,230,230)

    while True:

        #对函数调用

        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()

        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets,text, textRect)
        # screen.blit(text, textRect)
run_game()