# -*- coding=utf-8 -*-
# @Time: 2022/7/13 21:53
# @Author: John
# @File: game_functions.py
# @Software: PyCharm
import sys
import pygame
from Bullet import Bullet
from alien import Alien


def get_number_aliens_x(ai_settings,alien_width):
    avaliable_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(avaliable_space_x / (2 * alien_width))
    return number_aliens_x

def creat_alien(ai_settings,screen,aliens,alien_num):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_num
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(ai_settings,screen,aliens):
    alien=Alien(ai_settings,screen)
    alien_width = alien.rect.width
    number_aliens_x=get_number_aliens_x(ai_settings,alien_width)



    for alien_num in range(number_aliens_x):
        creat_alien(ai_settings, screen, aliens, alien_num)




def fire_bullets(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullets_allow:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keydown_events(event, ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()



def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # print("keydown")
            # check_keydown_events(event, ship)
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)






def update_screen(ai_settings,screen,ship,aliens,bullets,text,textRect):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    screen.blit(text, textRect)
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)