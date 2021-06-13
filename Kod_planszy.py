import sys
import pygame
pygame.init()

pygame.display.set_caption("destiny")
okno_width = 1280
okno_height = 720
okno = pygame.display.set_mode((okno_width, okno_height))

supermarket =[]

tlo = pygame.image.load('tlo.jpg')

class Sciany():
    def __init__(self, x, y, szerokosc, wysokosc):
        self.x = x
        self.y = y
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.hitbox = pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)
    def rysuj(self, okno):
        sciana.hitbox= pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)
        pygame.draw.rect(okno,(120,60,0), sciana.hitbox)

sciana = Sciany(0, 0, 30, 720)
supermarket.append(sciana)
sciana2 = Sciany(1250, 0, 30, 720)
supermarket.append(sciana2)
sciana3 = Sciany(30, 0, 1220, 30)
supermarket.append(sciana3)
sciana4 = Sciany(30, 690, 1220, 30)
supermarket.append(sciana4)
sciana5 = Sciany(180, 0, 30, 500)
supermarket.append(sciana5)
sciana6 = Sciany(180, 600, 30, 130)
supermarket.append(sciana6)
sciana7 = Sciany(420, 0, 30, 240)
supermarket.append(sciana7)
sciana8 = Sciany(420, 340, 30, 360)
supermarket.append(sciana8)
sciana9 = Sciany(600, 0, 30, 580)
supermarket.append(sciana9)
sciana10 = Sciany(800, 0, 30, 120)
supermarket.append(sciana10)
sciana11 = Sciany(800, 220, 30, 720)
supermarket.append(sciana11)
sciana12 = Sciany(1040, 0, 30, 315)
supermarket.append(sciana12)
sciana13 = Sciany(1040, 415, 30, 720)
supermarket.append(sciana13)

def okno_gry():
    okno.blit(tlo, (0,0))

    for sciana in supermarket:
        sciana.rysuj(okno)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


okno_gry()
