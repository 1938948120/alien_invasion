import sys

import pygame

def check_events():
    """相应按键和鼠标"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(init_setting, screen, ship):
    """更新屏幕上的图像"""
    # 背景色充满屏幕，每次循环重新绘制屏幕
    screen.fill(init_setting.bg_color)

    # 绘制飞船位置
    ship.blitme()

    # 刷新屏幕
    pygame.display.flip()