import sys
'''退出游戏用'''
import pygame
from settings import AlienSettings
from ship import Ship
from game_functions import check_events, update_screen


def run_game():
    pygame.init()
    init_setting = AlienSettings()
    screen = pygame.display.set_mode(
        (init_setting.screen_width, init_setting.screen_height))
    pygame.display.set_caption("Alien Invsion")

    # 创建飞船
    ship = Ship(screen)

    while True:

        check_events()
        update_screen(init_setting, screen, ship)


run_game()
