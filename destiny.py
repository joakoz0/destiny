import pygame
from pygame.locals import *
import sys
import random
pygame.init()

pygame.mixer.music.load('buy_mode.mp3')
pygame.mixer.music.play(-1)

pygame.display.set_caption("destiny")
okno_width = 1280
okno_height = 720
okno = pygame.display.set_mode((okno_width, okno_height))

supermarket =[]

idz_prawo = [pygame.image.load('prawo1.png'), pygame.image.load('prawo2.png')]
idz_lewo = [pygame.image.load('lewo1.png'), pygame.image.load('lewo2.png')]
idz_prosto = [pygame.image.load('3.png'), pygame.image.load('2.png')]
idz_tyl = [pygame.image.load('tyl1.png'), pygame.image.load('tyl2.png')]
stoj = pygame.image.load('1.png')

tlo = pygame.image.load('tlo.jpg')

image = pygame.image.load("rat.png")

clock = pygame.time.Clock()

class Bohater():
    def __init__(self, x, y, szerokosc, wysokosc):
        self.x=x
        self.y=y
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.ruch = 4
        self.lewo = False
        self.prawo = False
        self.prosto = False
        self.tyl = False
        self.licznik = 0
        self.bezruch=True
        self.hitbox=(self.x+8,self.y+12,70,70)
        self.zdrowko=50
        self.visible=True

    def ruchy_bohatera(self, okno):
        if self.visible==True:

            if self.licznik +2 >= 6:
                self.licznik = 0

            if not (self.bezruch):
                if self.lewo:
                    okno.blit(idz_lewo[self.licznik//3], (self.x,self.y))
                    self.licznik += 1
                elif self.prawo:
                    okno.blit(idz_prawo[self.licznik//3], (self.x,self.y))
                    self.licznik += 1
                elif self.prosto:
                    okno.blit(idz_prosto[self.licznik//3], (self.x,self.y))
                    self.licznik += 1
                elif self.tyl:
                    okno.blit(idz_tyl[self.licznik//3], (self.x,self.y))
                    self.licznik += 1
            else:
                if self.prawo:
                    okno.blit((idz_prawo[0]), (self.x, self.y))
                elif self.lewo:
                    okno.blit((idz_lewo[0]), (self.x, self.y))
                elif self.tyl:
                    okno.blit((idz_tyl[0]), (self.x, self.y))
                else:
                    okno.blit((idz_prosto[0]), (self.x, self.y))

            pygame.draw.rect(okno,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,50,10))
            pygame.draw.rect(okno,(0,255,0),(self.hitbox[0],self.hitbox[1]-20,(50-2*(50-self.zdrowko)),10))
            self.hitbox=pygame.Rect(self.x+8,self.y+12,70,70)
            # pygame.draw.rect(okno,(255,0,0),self.hitbox,2)

    def hit(self):
        if self.visible==True:

            self.x=620
            self.y=620
            if self.zdrowko!=30:
                self.zdrowko-=5
                czcionka1=pygame.font.SysFont("comicsans",100)
                napis=czcionka1.render("-5",1,(255,0,0))
                okno.blit(napis,(640-(napis.get_width()/2),350))
                pygame.display.update()
                i = 0
                while i < 100:
                    pygame.time.delay(10)
                    i += 1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            i = 101
                            pygame.quit()
            else:
                self.visible=False
                czcionka2=pygame.font.SysFont("comicsans",250)
                koniecgry=czcionka2.render("GAME OVER",1,(0,0,128))
                okno.blit(koniecgry,(640-(koniecgry.get_width()/2),350))
                pygame.display.update()
                i=0
                while i < 200:
                    pygame.time.delay(10)
                    i += 1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            i = 201
                            pygame.quit()

    def czy_sciana(self, okno):
        for sciana in supermarket:
            if pygame.Rect.colliderect(gracz.hitbox, sciana.hitbox):
                print("zakaz")

def okno_gry():
    okno.blit(tlo, (0,0))
    gracz.ruchy_bohatera(okno)
    gracz.czy_sciana(okno)
    szczur1.move(okno)
    szczur2.move(okno)
    szczur3.move(okno)
    szczur4.move(okno)
    szczur5.move(okno)
    szczur6.move(okno)

    for strzal in strzaly:
        strzal.draw(okno)

    for sciana in supermarket:
        sciana.rysuj(okno)

    pygame.display.update()

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

class Enemy():
    def __init__(self,x,y,e_width,e_height):

        self.x=x
        self.y=y
        self.e_width=e_width
        self.e_height=e_height
        self.vel = random.randint(2, 8)
        self.hitbox = (self.x + 17, self.y + 11, 30, 30)
        self.health=5
        self.visible=True


    def move(self,okno):

        if self.visible:
            if self.y < 32:
                self.vel = -self.vel
            if self.y > (okno_height-64):
                self.vel = -self.vel
            okno.blit(image, (self.x, self.y))
            self.y += self.vel

            pygame.draw.rect(okno,(255,0,0),(self.hitbox[0],self.hitbox[1]-20, 25,10))
            pygame.draw.rect(okno,(0,255,0),(self.hitbox[0],self.hitbox[1]-20, 25-5*(5-self.health),10))
            self.hitbox = pygame.Rect(self.x, self.y,30,30)
            #pygame.draw.rect(okno, (255,0,0), self.hitbox,3,25)


    def hit(self):
        if self.health>0:
            self.health-=1
        else:
            self.visible=False
        print("hit")
        pass


class pociski(object):
    def __init__(self,x,y,zasieg,kolor,kierunek):
        self.x=x
        self.y=y
        self.kolor=kolor
        self.zasieg=zasieg
        self.licznik=8
        self.kierunek=kierunek

    def ruchy(self):
        self.x += self.kierunek[0] * self.licznik
        self.y += self.kierunek[1] * self.licznik

    def draw(self,okno):
        pygame.draw.circle(okno,self.kolor,(self.x,self.y), self.zasieg)



gracz = Bohater(600, 600, 60, 60)

szczur1 = Enemy(120,200,20,20)
szczur2 = Enemy(280,400,20,20)
szczur3 = Enemy(480,600,20,20)
szczur4 = Enemy(700,200,20,20)
szczur5 = Enemy(870,400,20,20)
szczur6 = Enemy(950,600,20,20)

run = True
strzaly=[]
kierunek=(-1,0)
shootloop=0
czcionka = pygame.font.SysFont("comicsans", 30, True)

while run:
    clock.tick(16)

    if szczur1.visible==True:
        if gracz.hitbox[1]<szczur1.hitbox[1]+szczur1.hitbox[3] and gracz.hitbox[1]+gracz.hitbox[3]>szczur1.hitbox[1]:
            if gracz.hitbox[0]+gracz.hitbox[2]>szczur1.hitbox[0] and gracz.hitbox[0]<szczur1.hitbox[0]+szczur1.hitbox[2]:
                gracz.hit()

    if szczur2.visible==True:
        if gracz.hitbox[1]<szczur2.hitbox[1]+szczur2.hitbox[3] and gracz.hitbox[1]+gracz.hitbox[3]>szczur2.hitbox[1]:
            if gracz.hitbox[0]+gracz.hitbox[2]>szczur2.hitbox[0] and gracz.hitbox[0]<szczur2.hitbox[0]+szczur2.hitbox[2]:
                gracz.hit()

    if szczur3.visible==True:
        if gracz.hitbox[1]<szczur3.hitbox[1]+szczur3.hitbox[3] and gracz.hitbox[1]+gracz.hitbox[3]>szczur3.hitbox[1]:
            if gracz.hitbox[0]+gracz.hitbox[2]>szczur3.hitbox[0] and gracz.hitbox[0]<szczur3.hitbox[0]+szczur3.hitbox[2]:
                gracz.hit()

    if szczur4.visible==True:
        if gracz.hitbox[1]<szczur4.hitbox[1]+szczur4.hitbox[3] and gracz.hitbox[1]+gracz.hitbox[3]>szczur4.hitbox[1]:
            if gracz.hitbox[0]+gracz.hitbox[2]>szczur4.hitbox[0] and gracz.hitbox[0]<szczur4.hitbox[0]+szczur4.hitbox[2]:
                gracz.hit()

    if szczur5.visible==True:
        if gracz.hitbox[1]<szczur5.hitbox[1]+szczur5.hitbox[3] and gracz.hitbox[1]+gracz.hitbox[3]>szczur5.hitbox[1]:
            if gracz.hitbox[0]+gracz.hitbox[2]>szczur5.hitbox[0] and gracz.hitbox[0]<szczur5.hitbox[0]+szczur5.hitbox[2]:
                gracz.hit()

    if szczur6.visible==True:
        if gracz.hitbox[1]<szczur6.hitbox[1]+szczur6.hitbox[3] and gracz.hitbox[1]+gracz.hitbox[3]>szczur6.hitbox[1]:
            if gracz.hitbox[0]+gracz.hitbox[2]>szczur6.hitbox[0] and gracz.hitbox[0]<szczur6.hitbox[0]+szczur6.hitbox[2]:
                gracz.hit()



    if shootloop > 0:
        shootloop += 1
    if shootloop > 2:
        shootloop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

    for strzal in strzaly[:]:

        if szczur1.visible==True and strzal.y-strzal.zasieg<szczur1.hitbox[1]+szczur1.hitbox[3] and strzal.y+strzal.zasieg>szczur1.hitbox[1]:
            if strzal.x+strzal.zasieg>szczur1.hitbox[0] and strzal.x-strzal.zasieg<szczur1.hitbox[0]+szczur1.hitbox[2]:
                szczur1.hit()
                strzaly.remove(strzal)

        elif szczur2.visible==True and strzal.y-strzal.zasieg<szczur2.hitbox[1]+szczur2.hitbox[3] and strzal.y+strzal.zasieg>szczur2.hitbox[1]:
            if strzal.x+strzal.zasieg>szczur2.hitbox[0] and strzal.x-strzal.zasieg<szczur2.hitbox[0]+szczur2.hitbox[2]:
                szczur2.hit()
                strzaly.remove(strzal)

        elif szczur3.visible==True and strzal.y-strzal.zasieg<szczur3.hitbox[1]+szczur3.hitbox[3] and strzal.y+strzal.zasieg>szczur3.hitbox[1]:
            if strzal.x+strzal.zasieg>szczur3.hitbox[0] and strzal.x-strzal.zasieg<szczur3.hitbox[0]+szczur3.hitbox[2]:
                szczur3.hit()
                strzaly.remove(strzal)

        elif szczur4.visible==True and strzal.y-strzal.zasieg<szczur4.hitbox[1]+szczur4.hitbox[3] and strzal.y+strzal.zasieg>szczur4.hitbox[1]:
            if strzal.x+strzal.zasieg>szczur4.hitbox[0] and strzal.x-strzal.zasieg<szczur4.hitbox[0]+szczur4.hitbox[2]:
                szczur4.hit()
                strzaly.remove(strzal)

        elif szczur5.visible==True and strzal.y-strzal.zasieg<szczur5.hitbox[1]+szczur5.hitbox[3] and strzal.y+strzal.zasieg>szczur5.hitbox[1]:
            if strzal.x+strzal.zasieg>szczur5.hitbox[0] and strzal.x-strzal.zasieg<szczur5.hitbox[0]+szczur5.hitbox[2]:
                szczur5.hit()
                strzaly.remove(strzal)

        elif szczur6.visible==True and strzal.y-strzal.zasieg<szczur6.hitbox[1]+szczur6.hitbox[3] and strzal.y+strzal.zasieg>szczur6.hitbox[1]:
            if strzal.x+strzal.zasieg>szczur6.hitbox[0] and strzal.x-strzal.zasieg<szczur6.hitbox[0]+szczur6.hitbox[2]:
                szczur6.hit()
                strzaly.remove(strzal)

        if strzal.x<1280 and strzal.x>0 and strzal.y<720 and strzal.y>0:
            strzal.ruchy()
        else:
            strzaly.remove(strzal)

    klawisz = pygame.key.get_pressed()

    if klawisz[pygame.K_LEFT]:
        gracz.x -= gracz.ruch
        gracz.lewo = True
        gracz.prawo = False
        gracz.tyl = False
        gracz.prosto = False
        gracz.bezruch=False
        for sciana in supermarket:
            if pygame.Rect.colliderect(gracz.hitbox, sciana.hitbox):
                print("prosze przestać :(")
                #self.licznik += 0
                #gracz.x -= gracz.ruch
                # gracz.lewo = False
                # gracz.bezruch = True

    elif klawisz[pygame.K_RIGHT]:
        gracz.x += gracz.ruch
        gracz.prawo = True
        gracz.lewo = False
        gracz.tyl = False
        gracz.prosto = False
        gracz.bezruch=False
        for sciana in supermarket:
            if gracz.hitbox.colliderect(sciana.hitbox):
                print("prosze przestać :(")

    elif klawisz[pygame.K_UP]:
        gracz.y -= gracz.ruch
        gracz.prosto = True
        gracz.lewo = False
        gracz.prawo = False
        gracz.tyl = False
        gracz.bezruch=False
        for sciana in supermarket:
            if gracz.hitbox.colliderect(sciana.hitbox):
                print("prosze przestać :(")

    elif klawisz[pygame.K_DOWN]:
        gracz.y += gracz.ruch
        gracz.tyl = True
        gracz.prosto = False
        gracz.lewo = False
        gracz.prawo = False
        gracz.bezruch=False
        for sciana in supermarket:
            if gracz.hitbox.colliderect(sciana.hitbox):
                print("prosze przestać :(")

    elif klawisz[pygame.K_SPACE] and shootloop==0:
        if gracz.lewo:
            kierunek=(-1,0)
        elif gracz.prawo:
            kierunek=(1,0)
        elif gracz.prosto:
            kierunek=(0,-1)
        elif gracz.tyl:
            kierunek=(0,1)

        if len(strzaly) < 15:
            strzaly.append(pociski(round(gracz.x+gracz.szerokosc//2), round(gracz.y+gracz.wysokosc//2),6,(255,0,0),kierunek))
        shootloop+=1
    else:
        gracz.bezruch=True


    szczur1.move(okno)
    szczur2.move(okno)
    szczur3.move(okno)
    szczur4.move(okno)
    szczur5.move(okno)
    szczur6.move(okno)


    okno_gry()
