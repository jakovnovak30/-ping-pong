import pygame
import igrac
import lopta
import random
import math

pygame.init()
ekran = pygame.display.set_mode((700, 500))
pygame.display.set_caption('ping(pong)')
pygame.display.update()

def igra():
    skor1 = 0
    skor2 = 0
    igrac1 = igrac.Plejer((50,200), (50,300))
    igrac2 = igrac.Plejer((650,200), (650,300))
    lopta1 = lopta.Lopta((350,300))

    igrac1.nacrtaj(ekran)
    igrac2.nacrtaj(ekran)
    lopta1.nacrtaj(ekran)
    bg = pygame.image.load("pong.jpeg")

    vura = pygame.time.Clock()

    while True:
        ekran.blit(bg, (0,0))
        mesg1 = pygame.font.SysFont("retrogaming", 30).render('Skor1: ' + str(skor1), True, (255,255,255))
        mesg2 = pygame.font.SysFont("retrogaming", 30).render('Skor2: ' + str(skor2), True, (255,255,255))
        ekran.blit(mesg1, [20, 40])
        ekran.blit(mesg2, [600, 40])

        tipke = pygame.key.get_pressed()

        if tipke[pygame.K_DOWN]:
            igrac2.dole(ekran)
        elif tipke[pygame.K_UP]:
            igrac2.gore(ekran)

        if tipke[pygame.K_w]:
            igrac1.gore(ekran)
        elif tipke[pygame.K_s]:
            igrac1.dole(ekran)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if igrac1.t1[0] + 13 >= lopta1.k[0] and (lopta1.zadnji == 2 or lopta1.zadnji == 0):
            if igrac1.t1[1] <= lopta1.k[1] and igrac1.t2[1] >= lopta1.k[1]:
                lopta1.zadnji = 1

                odsredine = min(abs(lopta1.k[1] - igrac1.t2[1]), abs(lopta1.k[1] - igrac1.t1[1]))
                if odsredine != 0: kut = math.atan(8/odsredine)
                else:
                    kut = math.pi
                brzina = math.sqrt(pow(lopta1.brzinah, 2) + pow(lopta1.brzinav, 2))

                lopta1.brzinah = brzina*math.cos(kut)

                lopta1.brzina = brzina*math.sin(kut)

        elif igrac2.t1[0] <= lopta1.k[0] + 13 and (lopta1.zadnji == 1 or lopta1.zadnji == 0):
            if igrac2.t1[1] <= lopta1.k[1] and igrac2.t2[1] >= lopta1.k[1]:
                lopta1.zadnji = 2

                odsredine = min(abs(lopta1.k[1] - igrac2.t2[1]), abs(lopta1.k[1] - igrac2.t1[1]))
                if odsredine != 0: kut = math.atan(8/odsredine)
                else:
                    kut = math.pi

                brzina = math.sqrt(pow(lopta1.brzinah, 2) + pow(lopta1.brzinav, 2))

                lopta1.brzinah = -1*brzina*math.cos(kut)

                lopta1.brzinav = -1*brzina*math.sin(kut)

        promjena = lopta1.update(ekran)

        if promjena != -1:
            if promjena == 1:
                skor1 = skor1 + 1
            elif promjena == 2:
                skor2 = skor2 + 1
            lopta1 = lopta1 = lopta.Lopta((350,300))

        lopta1.nacrtaj(ekran)
        igrac1.nacrtaj(ekran)
        igrac2.nacrtaj(ekran)

        pygame.display.update()
        vura.tick(30)

#vuzgi igru
igra()
