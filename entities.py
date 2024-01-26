import random
import pygame
from colors import *
from main import WIDTH, HEIGHT, FPS


class Obstacle:
    

    def __init__(self):
        self.size = 80
        self.speed = 12
        self.color = DimGrey
        self.rect = pygame.Rect(WIDTH, HEIGHT * 2 / 3 - self.size, self.size, self.size)
        self.texture = pygame.image.load("sprites/obstacle/body.png")

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
        self.size = 40
        self.speed = 10
        self.current_speed = 0
        self.jump_speed = 15
        self.jumping = False
        self.jump_count = 0
        self.start_speed = self.jump_speed
        self.color = Crimson
        self.rect = pygame.Rect(WIDTH / 2, HEIGHT * 2 / 3 - self.size, self.size, self.size)
        self.texture = pygame.image.load("sprites/player/body.png")


    def move(self, keys):
        self.rect.x += self.current_speed

        if self.current_speed > 0 :
            self.current_speed -= self.speed*0.025
        elif self.current_speed < 0:
            self.current_speed += self.speed*0.025
        else:
            self.current_speed = 0

        if keys[pygame.K_LEFT]:
            if self.current_speed > -self.speed:
                self.current_speed -= self.speed*0.1
        if keys[pygame.K_RIGHT]:
            if self.current_speed < self.speed:
                self.current_speed += self.speed*0.1

        if self.rect.x < 0:
            self.rect.x = WIDTH
        elif self.rect.x > WIDTH:
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