# -*- coding=utf-8 -*-
# @Time: 2022/7/13 21:53
# @Author: John
# @File: game_functions.py
# @Software: PyCharm
import sys
import pygame
from Bullet import Bullet
from alien import Alien
import time

# def update_bullets(bullets):
#     bullets.update()
#
#     for bullet in bullets.copy():
#         if bullet.rect.bottom <= 0:
#             bullets.remove(bullet)

def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):

    collisions=pygame.sprite.groupcollide(bullets,aliens,False,True)
    if (len(aliens)==0):

        bullets.empty()
        # time.sleep(1)
        create_fleet(ai_settings,screen,ship,aliens)


def update_bullet(ai_settings,screen,ship,aliens,bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break


def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):

    stats.ship_left -= 1
    print("stats.ship_left"+str(stats.ship_left))

    aliens.empty()
    bullets.empty()

    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():

        if alien.rect.bottom >=  screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break




def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship,aliens):
        check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def get_number_aliens_y(ai_settings,alien_height,ship):
    ship_height = ship.rect.height
    avaliable_space_y = ai_settings.screen_height - 3 * alien_height -2 * ship_height
    number_aliens_y = int(avaliable_space_y / (2 * alien_height))
    return number_aliens_y


def get_number_aliens_x(ai_settings,alien_width):
    avaliable_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(avaliable_space_x / (2 * alien_width))
    return number_aliens_x

def creat_alien(ai_settings,screen,aliens,alien_num,row_num):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_num
    alien.y = alien_height + 2 * alien_height * row_num
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    alien=Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    number_aliens_x=get_number_aliens_x(ai_settings,alien_width)
    number_aliens_y=get_number_aliens_y(ai_settings,alien_height,ship)
    print("number_aliens_y",number_aliens_y,"number_aliens_x",number_aliens_x)



    for row_num in range(number_aliens_y):
        for alien_num in range(number_aliens_x):
            creat_alien(ai_settings, screen, aliens, alien_num,row_num)




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


