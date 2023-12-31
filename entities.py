import random
import pygame
from colors import *
from main import WIDTH, HEIGHT, FPS


class Obstacle:
    

    def __init__(self):
        self.size = 50
        self.speed = 12
        self.color = DimGrey
        self.rect = pygame.Rect(WIDTH, HEIGHT * 2 / 3 - self.size, self.size, self.size)

    def move(self):
        self.rect.x -= self.speed
        if self.rect.x < -self.size or self.rect.x > WIDTH:
            self.reset()

    def reset(self):
        variant = random.randint(0,1)
        if variant == 0:
            self.rect.x = WIDTH           
        else:
            self.rect.x = -self.size
            self.speed *= -1
        self.rect.y = HEIGHT * 2 / 3 - self.size

class Player:
    
    def __init__(self):
        self.size = 25
        self.speed = 10
        self.jump_speed = 15
        self.start_speed = self.jump_speed
        self.color = Crimson
        self.rect = pygame.Rect(WIDTH / 2, HEIGHT * 2 / 3 - self.size, self.size, self.size)
        self.jumping = False
        self.jump_count = 0

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.rect.x = WIDTH
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            if self.rect.x > WIDTH:
                self.rect.x = 0

    def jump(self, keys):
        if not self.jumping:
            if keys[pygame.K_UP]:
                self.jumping = True
        else:
            if self.jump_speed >= -self.start_speed:
                self.rect.y -= self.jump_speed
                self.jump_speed -= 1
            else:
                self.jump_speed = self.start_speed
                self.jumping = False

                
                

                

if __name__ == "__main__":
    pass