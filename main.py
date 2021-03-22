import pygame
import igrac
import lopta
import random
import math

pygame.init()
ekran = pygame.display.set_mode((700, 500))
pygame.display.set_caption('ping(pong)')
pygame.display.update()
vura = pygame.time.Clock()
pocetak = False

mesg1 = pygame.font.SysFont("retrogaming", 60).render('(Ping)Pong', True, (255,255,255))
ekran.blit(mesg1, [250, 100])
slika = pygame.image.load("pocetna.png")
ekran.blit(slika, (200,250))
x = 0
while not pocetak:
    x = x + 1
    if x%2 == 1:
        mesg2 = pygame.font.SysFont("retrogaming", 30).render('Press any key to start', True, (255,255,255))
        ekran.blit(mesg2, [250, 200])
    else:
        pygame.draw.rect(ekran, (0,0,0), [250, 200, 250, 30])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            pocetak = True

    pygame.display.update()
    vura.tick(6)

ekran.fill((0,0,0))
mesg = pygame.font.SysFont("retrogaming", 35).render('Za singleplayer pritisnite 1, a za multi 2', True, (255,255,255))
ekran.blit(mesg, [100,200])
pygame.display.update()
game_mode = -1
while game_mode == -1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                game_mode = 1
            elif event.key == pygame.K_2:
                game_mode = 2

def igra():
    traje = True
    pobednik = 0
    skor1 = 0
    skor2 = 0
    igrac1 = igrac.Plejer((50,200), (50,300))
    igrac2 = igrac.Plejer((650,200), (650,300))
    lopta1 = lopta.Lopta((350,300))

    igrac1.nacrtaj(ekran)
    igrac2.nacrtaj(ekran)
    lopta1.nacrtaj(ekran)
    bg = pygame.image.load("pong.jpeg")
    while traje:
        ekran.blit(bg, (0,0))
        mesg1 = pygame.font.SysFont("retrogaming", 30).render('Skor1: ' + str(skor1), True, (255,255,255))
        mesg2 = pygame.font.SysFont("retrogaming", 30).render('Skor2: ' + str(skor2), True, (255,255,255))
        ekran.blit(mesg1, [100, 40])
        ekran.blit(mesg2, [530, 40])

        tipke = pygame.key.get_pressed()

        if tipke[pygame.K_DOWN]:
            igrac2.dole(ekran)
        elif tipke[pygame.K_UP]:
            igrac2.gore(ekran)

        if game_mode == 2:
            if tipke[pygame.K_w]:
                igrac1.gore(ekran)
            elif tipke[pygame.K_s]:
                igrac1.dole(ekran)
        else:
            sredina = round((igrac1.t1[1]+igrac1.t2[1])/2)
            if sredina + 15 < lopta1.k[1]:
                igrac1.dole(ekran)
            elif sredina - 15 > lopta1.k[1]:
                igrac1.gore(ekran)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if igrac1.t1[0] + 13 >= lopta1.k[0]:
            if igrac1.t1[1] <= lopta1.k[1] and igrac1.t2[1] >= lopta1.k[1]:
                odsredine = min(abs(lopta1.k[1] - igrac1.t2[1]), abs(lopta1.k[1] - igrac1.t1[1]))
                kut = math.atan((8+abs(lopta1.brzinav))/(odsredine+lopta1.brzinah))

                brzina = math.sqrt(pow(lopta1.brzinah, 2) + pow(lopta1.brzinav, 2))

                lopta1.brzinah = brzina*math.cos(kut)

                lopta1.brzina = brzina*math.sin(kut)

        elif igrac2.t1[0] <= lopta1.k[0] + 13:
            if igrac2.t1[1] <= lopta1.k[1] and igrac2.t2[1] >= lopta1.k[1]:
                odsredine = min(abs(lopta1.k[1] - igrac2.t2[1]), abs(lopta1.k[1] - igrac2.t1[1]))
                kut = math.atan((8+abs(lopta1.brzinav))/(odsredine+lopta1.brzinah))

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

        if skor1 >= 10:
            traje = False
            pobednik = 1
        elif skor2 >= 10:
            traje = False
            pobednik = 2

        lopta1.nacrtaj(ekran)
        igrac1.nacrtaj(ekran)
        igrac2.nacrtaj(ekran)

        pygame.display.update()
        vura.tick(30)

    while True:
        ekran.fill((0,0,0))
        mesg1 = pygame.font.SysFont("retrogaming", 55).render('Plejer ' + str(pobednik) + ' won!', True, (255,255,255))
        mesg2 = pygame.font.SysFont("retrogaming", 40).render('Press r to replay or q to quit.', True, (255,255,255))
        ekran.blit(mesg1, [50, 200])
        ekran.blit(mesg2, [50, 300])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_r:
                    igra()
        vura.tick(20)
#vuzgi igru
igra()
