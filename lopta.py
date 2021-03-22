import pygame
import random

class Lopta:
    def __init__(self, tocka):
        self.k = tocka

        smjer1 = random.randrange(0,1)
        smjer2 = random.randrange(0,1)

        if smjer1 == 0:
            self.brzinah = random.randrange(-8, -4)
        else:
            self.brzinah = random.randrange(4, 8)

        if smjer2 == 0:
            self.brzinav = random.randrange(-8, 4)
        else:
            self.brzinav = random.randrange(4, 8)    

        self.zadnji = 0 #ko je zadnji diral loptu

    def nacrtaj(self, ekran):
        pygame.draw.circle(ekran, (255,255,255), self.k, 8)

    def update(self, ekran):
        pygame.draw.circle(ekran, (0,0,0), self.k, 8)

        x = self.k[0]
        y = self.k[1]

        y = y + self.brzinav
        x = x + round(self.brzinah*1.5)

        if x < 0 or x > 700 or y < 45 or y > 500:
            return self.zadnji

        self.k = (x,y)
        return -1
