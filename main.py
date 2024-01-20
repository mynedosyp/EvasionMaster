import pygame
import sys
from entities import *
from colors import *

pygame.init()
# Получаем информацию о дисплее
infoObject = pygame.display.Info()

# Размер экрана
WIDTH = 800
HEIGHT = 600

# Константы
FPS = 60


class Game:

    def __init__(self):
        
        # Создание окна
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # Создание персонажа
        self.player = Player()

        # Создание препятствия
        self.obstacle = Obstacle()

        # Создание часов
        self.clock = pygame.time.Clock()
        self.frame_num = 0
        
        # Очки
        self.score = 0
        self.max_score = 0
        # Цвета
        self.ground_color = ForestGreen
        self.background_color = SkyBlue

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def check_collision(self):
        # Проверяем, произошла ли коллизия между игроком и препятствием
        if self.player.rect.colliderect(self.obstacle.rect):
            # Если произошла коллизия, то игрок перестает прыгать
            self.player.jumping = False
            self.player.jump_speed = self.player.start_speed
            # Возвращаем игрока на начальную позицию
            self.player.rect = pygame.Rect(self.player.rect.x, HEIGHT * 2 / 3 - self.player.size, self.player.size, self.player.size)        
            # Обновление рекорда
            if self.score > self.max_score:
                self.max_score = self.score
            # Обнуляем счет
            self.score = 0
            
        else:
            # Если не произошла коллизия, то проверяем, прошло ли 60 кадров (1 секунда)
            if self.frame_num in range(0, FPS, FPS//4):
                self.score += 1

    def draw_background(self):
        # Отрисовка фона
        self.screen.fill(self.background_color)  

        # Отрисовка земли
        pygame.draw.rect(self.screen, self.ground_color, pygame.Rect(0, HEIGHT / 3 * 2, WIDTH, HEIGHT / 3))  

    def draw_player(self):
        pygame.draw.rect(self.screen, self.player.color, self.player.rect)

    def draw_obstacle(self):
        pygame.draw.rect(self.screen, self.obstacle.color, self.obstacle.rect)

    def draw_score(self):
        font = pygame.font.SysFont('comicsans', 36)
        text = font.render(f"Score: {self.score}", 1, White)    
        outline = font.render(f"Score: {self.score}", 1, Black)
        x,y = 0 + 20, HEIGHT - text.get_height() - 20
        # Отрисовка обводки
        for dx, dy in [(-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2), (-1, -2), (-1, 2), (0, -2), (0, 2), (1, -2), (1, 2), (2, -2), (2, -1), (2, 0), (2, 1), (2, 2)]:
            self.screen.blit(outline, (x + dx, y + dy)) 
        # Отрисовка текста
        self.screen.blit(text, (x, y))

    def draw_record(self):
        font = pygame.font.SysFont('comicsans', 36)
        text = font.render(f"Session record: {self.max_score}", 1, White)    
        outline = font.render(f"Session record: {self.max_score}", 1, Black)
        x,y = WIDTH-text.get_width() - 20, HEIGHT - text.get_height() - 20
        # Отрисовка обводки
        for dx, dy in [(-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2), (-1, -2), (-1, 2), (0, -2), (0, 2), (1, -2), (1, 2), (2, -2), (2, -1), (2, 0), (2, 1), (2, 2)]:
            self.screen.blit(outline, (x + dx, y + dy))
        # Отрисовка текста
        self.screen.blit(text, (WIDTH-text.get_width() - 20, HEIGHT - text.get_height() - 20))

    def draw_screen(self):
        self.draw_background()
        self.draw_player()
        self.draw_obstacle()
        self.draw_score()
        self.draw_record()
        pygame.display.flip()

    def count_frame(self):
        self.frame_num += 1
        if self.frame_num == FPS+1:
            self.frame_num = 0

    def run(self):
        while True:
            keys = pygame.key.get_pressed()
            self.count_frame()
            self.handle_events()          
            self.player.move(keys)
            self.player.jump(keys)
            self.obstacle.move()
            self.check_collision()
            self.draw_screen()

            # Ограничение FPS
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()