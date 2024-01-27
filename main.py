import pygame
import sys
import toml
from entities import *
from colors import *


# Открытие файла pyproject.toml
with open('pyproject.toml', 'r') as file:
    # Чтение файла в формате TOML
    data = toml.load(file)

# Получение версии проекта
version = data['tool']['poetry']['version']


pygame.init()
# Получаем информацию о дисплее
infoObject = pygame.display.Info()
button_image = pygame.image.load('sprites/fullscreen.png')
button_x = 10
button_y = 10


# Размер экрана
WIDTH = 1920//2
HEIGHT = 1080//2

# Константы
FPS = 60


class Game:

    def __init__(self):
        
        # Создание окна
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # Флаг полноэкранного режима
        self.fullscreen = False
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
        global WIDTH, HEIGHT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
                # Проверка нажатия на кнопку
                # if event.pos[0] > button_x and event.pos[0] < button_x + button_image.get_width():
                #     if event.pos[1] > button_y and event.pos[1] < button_y + button_image.get_height():
                #         # Переключение режима полноэкранного/окна
                #         if self.fullscreen:
                #             #WIDTH, HEIGHT = 1920//2, 1080//2
                #             self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
                #             self.fullscreen = False
                #         else:
                #             #WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
                #             self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                #             self.fullscreen = True
            
    def draw_gui(self):
        self.screen.blit(button_image, (button_x, button_y))

    def record_update(self):
        # Обновление рекорда
        if self.score > self.max_score:
            self.max_score = self.score     

    def check_collision(self):
        # Проверяем, произошла ли коллизия между игроком и препятствием
        self.background_color = SkyBlue
        if self.player.rect.colliderect(self.obstacle.rect):
            self.background_color=(255,0,0)
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
        if abs(self.player.jump_speed) != 15:
            if 14 >= abs(self.player.jump_speed) > 12:
                self.player.texture = self.player.anim[6]
            elif 12 >= abs(self.player.jump_speed) > 10 :
                self.player.texture = self.player.anim[7]
            elif 10 >= abs(self.player.jump_speed) > 8 :
                self.player.texture = self.player.anim[8]
            elif 8 >= abs(self.player.jump_speed) >= 0 :
                self.player.texture = self.player.anim[9]
            else:
                self.player.texture = self.player.anim[0]
        else:
            if self.player.current_speed > 0 :
                self.player.texture = pygame.transform.flip(self.player.anim[self.frame_num//12], True, False)
            elif self.player.current_speed < 0:
                self.player.texture = pygame.transform.flip(self.player.anim[self.frame_num//12], False, False) 
            else:
                self.player.texture = self.player.anim[0]  
            
            
        self.player.texture = pygame.transform.scale(self.player.texture, (self.player.size, self.player.size))
        self.screen.blit(self.player.texture, (self.player.rect.x, self.player.rect.y))
        #pygame.draw.rect(self.screen, self.player.color, self.player.rect,2)

    def draw_obstacle(self):
        self.obstacle.texture = pygame.transform.scale(self.obstacle.texture, (self.obstacle.size, self.obstacle.size))     
        self.screen.blit(pygame.transform.rotate(self.obstacle.texture, 360/FPS*self.frame_num*(self.obstacle.speed/abs(self.obstacle.speed))),
                         (self.obstacle.rect.x-10, self.obstacle.rect.y-10))
        #pygame.draw.rect(self.screen, self.obstacle.color, self.obstacle.rect,2)

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
        #self.draw_gui()
        self.draw_player()
        self.draw_obstacle()
        self.draw_score()
        self.draw_record()
        pygame.display.set_caption(f"Evasion master v {version}, ({self.clock.get_fps():.3})")    
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
            self.record_update()
            self.draw_screen()
        
            # Ограничение FPS
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()