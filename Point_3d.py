# -*- coding: utf-8 -*-
import math
from Point import Point

class Point3d(Point):

    def __init__(self, X=0.0, Y=0.0, Z=0.0):
        # Наследование от класса Point
        Point.__init__(self, X, Y)
        self.coordZ = Z

    def getZ(self):
        return self.coordZ

    #Вычисление расстояние между точками
    def distanceTo(self, Point_2):
        return math.sqrt(((self.coordX - Point_2.getX()) ** 2) + ((self.coordY - Point_2.getY()) ** 2) + ((self.coordZ - Point_2.getZ()) ** 2))

    #Вывод координат
    def showInfo(self):
        print(self.coordX, self.coordY, self.coordZ)


