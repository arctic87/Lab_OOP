
# -*- coding: utf-8 -*-


class Point:

    def __init__(self, X, Y):
        self.coordX = X
        self.coordY = Y

    def getX(self):
        return self.coordX

    def getY(self):
        return self.coordY

    def setX(self, a):
        self.coordX = a

    def setY(self, b):
        self.coordY = b