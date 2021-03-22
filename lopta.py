import pygame
import random

class Lopta:
    def __init__(self, tocka):
        self.k = tocka

        smjer1 = random.randrange(0,2)
        smjer2 = random.randrange(0,2)

        if smjer1 == 0:
            self.brzinah = random.randrange(-8, -5)
        else:
            self.brzinah = random.randrange(5, 8)

        if smjer2 == 0:
            self.brzinav = random.randrange(-4, -2)
        else:
            self.brzinav = random.randrange(2, 4)

    def nacrtaj(self, ekran):
        pygame.draw.circle(ekran, (255,255,255), self.k, 8)

    def update(self, ekran):
        pygame.draw.circle(ekran, (0,0,0), self.k, 8)

        x = self.k[0]
        y = self.k[1]

        y = y + self.brzinav
        x = x + round(self.brzinah*1.5)

        if x < 45:
            return 2
        elif x > 655:
            return 1
        if y < 0 or y > 500:
            self.brzinav *= -1

        self.k = (x,y)
        return -1
