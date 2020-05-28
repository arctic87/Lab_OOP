# -*- coding: utf-8 -*-
import math
from Point import Point

class Triangle(Point):
    def __init__(self,X,Y,X1,Y1,X2,Y2):
        Point.__init__(self, X,Y)
        self.coordX1 = X1
        self.coordY1 = Y1
        self.coordX2 = X2
        self.coordY2 = Y2

    def getX1(self):
        return self.coordX1

    def getY1(self):
        return self.coordY1

    def getX2(self):
        return self.coordX2

    def getY2(self):
        return self.coordY2

    def showInfo(self):
        print("Координаты вершин треугольника:""X=",self.coordX, "Y=",self.coordY, "X1=",self.coordX1, "Y1=",self.coordY1, "X2=",self.coordX, "Y2=",self.coordY )

    def area(self):
        return abs(self.coordX * (self.coordY1 - self.coordY2) + self.coordX1 * (self.coordY2 - self.coordY) + self.coordX2 * (self.coordY - self.coordY1)) / 2.0
        print('Площадь:',self.area)
