import pygame
from colors import *

pygame.init()
# Получаем информацию о дисплее
infoObject = pygame.display.Info()

# Размер экрана
WIDTH = 800
HEIGHT = 600

# Константы
FPS = 60


screen = pygame.display.set_mode((WIDTH, HEIGHT))

player_polygons = [
                    [40, 10],
                    [50, 20], 
                    [40, 30],
                    [50, 30], 
                    [80, 40],
                    [50, 40], 
                    [40, 60],
                    [50, 90], 
                    [40, 70],
                    [30, 90], 
                    [40, 60],
                    [30, 40], 
                    [0, 40],
                    [30, 30], 
                    [40, 30], 
                    [30, 20], 
                    [40, 10],
                   ]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill(Black)
    pygame.draw.polygon(screen, White, player_polygons)
    pygame.display.flip()