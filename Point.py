# -*- coding: utf-8 -*-


class Point:
    #Задаем координаты
    def __init__(self, X=0.0, Y=0.0):
        self.coordX = X
        self.coordY = Y

    def getX(self):
        return self.coordX

    def getY(self):
        return self.coordY
