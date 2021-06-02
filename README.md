import pygame
pygame.init()

okno = pygame.display.set_mode((1280,720))

idz_prawo = [pygame.image.load('prawo1.png'), pygame.image.load('prawo2.png')]
idz_lewo = [pygame.image.load('lewo1.png'), pygame.image.load('lewo2.png')]
idz_prosto = [pygame.image.load('3.png'), pygame.image.load('2.png')]
idz_tyl = [pygame.image.load('tyl1.png'), pygame.image.load('tyl2.png')]

tlo = pygame.image.load('tlo.jpg')
stoj = pygame.image.load('1.png')

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

    def ruchy_bohatera(self, okno):

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


def okno_gry():
    okno.blit(tlo, (0,0))
    gracz.ruchy_bohatera(okno)

    for strzal in strzaly:
        strzal.draw(okno)


    pygame.display.update()


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


#główna część
gracz = Bohater(600, 600, 60, 60)
run = True
strzaly=[]
kierunek=(-1,0)

while run:
    clock.tick(16)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for strzal in strzaly[:]:
        if strzal.x<1280 and strzal.x>0 and strzal.y<720 and strzal.y>0:
            strzal.ruchy()
        else:
            strzaly.pop(strzaly.index(strzal))

    klawisz = pygame.key.get_pressed()

    if klawisz[pygame.K_LEFT]:
        gracz.x -= gracz.ruch
        gracz.lewo = True
        gracz.prawo = False
        gracz.tyl = False
        gracz.prosto = False
        gracz.bezruch=False

    elif klawisz[pygame.K_RIGHT]:
        gracz.x += gracz.ruch
        gracz.prawo = True
        gracz.lewo = False
        gracz.tyl = False
        gracz.prosto = False
        gracz.bezruch=False

    elif klawisz[pygame.K_UP]:
        gracz.y -= gracz.ruch
        gracz.prosto = True
        gracz.lewo = False
        gracz.prawo = False
        gracz.tyl = False
        gracz.bezruch=False

    elif klawisz[pygame.K_DOWN]:
        gracz.y += gracz.ruch
        gracz.tyl = True
        gracz.prosto = False
        gracz.lewo = False
        gracz.prawo = False
        gracz.bezruch=False

    elif klawisz[pygame.K_SPACE]:
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
    else:
        gracz.bezruch=True


    okno_gry()

pygame.quit()
