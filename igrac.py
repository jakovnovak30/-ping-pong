import pygame

class Plejer:
    def __init__(self, tocka1, tocka2):
        self.t1 = tocka1
        self.t2 = tocka2

    def nacrtaj(self, ekran):
        pygame.draw.line(ekran, (255,255,255), self.t1, self.t2, 10)

    def dole(self, ekran):
        pygame.draw.line(ekran, (0,0,0), self.t1, self.t2, 10)

        x1 = self.t1[0]
        y1 = self.t1[1] + 7

        x2 = self.t2[0]
        y2 = self.t2[1] + 7

        if y2 <= 495:
            self.t1 = (x1, y1)
            self.t2 = (x2, y2)
            return
        else:
            return

    def gore(self, ekran):
        pygame.draw.line(ekran, (0,0,0), self.t1, self.t2, 10)

        x1 = self.t1[0]
        y1 = self.t1[1] - 7

        x2 = self.t2[0]
        y2 = self.t2[1] - 7

        if y1 >= 45:
            self.t1 = (x1, y1)
            self.t2 = (x2, y2)
            return
        else:
            return
