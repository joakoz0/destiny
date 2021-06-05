import pygame
from pygame.locals import *
import sys
import random

pygame.init()


vec = pygame.math.Vector2
width = 1000
height = 800
screen = pygame.display.set_mode((width, height))
fps = 60
fps_clock = pygame.time.Clock()

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def render(self):
        screen.blit(self.bgimage, (self.bgX, self.bgY))


class Enemy(pygame.sprite.Sprite):


    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("rat (1).png")
        self.rect = self.image.get_rect()
        self.pos = vec(0, 0)
        self.vel = vec(0, 0)
        self.vel.x = random.randint(2, 8)
        self.vel.y = random.randint(2, 8)
        self.spawn = random.randint(1, 7)
        if self.spawn == 1:
            self.pos.x = 150
            self.pos.y = 200
        if self.spawn == 2:
            self.pos.x = 150
            self.pos.y = 400
        if self.spawn == 3:
            self.pos.x = 150
            self.pos.y = 600
        if self.spawn == 4:
            self.pos.x = 850
            self.pos.y = 200
        if self.spawn == 5:
            self.pos.x = 850
            self.pos.y = 400
        if self.spawn == 6:
            self.pos.x = 850
            self.pos.y = 600
    def move(self):
        if self.pos.y < 0:
            self.vel.y = -self.vel.y
        if self.pos.y > (height-32):
            self.vel.y = -self.vel.y
        if self.pos.x < 0:
            self.vel.x = -self.vel.x
        if self.pos.x> (width-32):
            self.vel.x = -self.vel.x
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
        self.rect.center = self.pos

    def render(self):
        screen.blit(self.image, (self.pos.x, self.pos.y))

szczur1 = Enemy()
szczur2 = Enemy()
szczur3 = Enemy()
szczur4 = Enemy()
szczur5 = Enemy()
szczur6 = Enemy()
szczur7 = Enemy()
szczur8 = Enemy()

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    szczur1.render()
    szczur1.move()
    szczur2.render()
    szczur2.move()
    szczur3.render()
    szczur3.move()
    szczur4.render()
    szczur4.move()
    szczur5.render()
    szczur5.move()
    szczur6.render()
    szczur6.move()
    szczur7.render()
    szczur7.move()
    szczur8.render()
    szczur8.move()

    pygame.display.update()
    fps_clock.tick(fps)
