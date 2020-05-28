# -*- coding: utf-8 -*-
import math
from Point import Point

class Point3d(Point):

    def __init__(self, X=0.0, Y=0.0, Z=0.0):

        Point.__init__(self, X, Y)
        self.coordZ = Z

    def getZ(self):
        return self.coordZ

    def getXYZ(self):
        return self.coordX, self.coordY, self.coordZ

    def setZ(self, c):
        self.coordZ = c

    def equals(self, O):
        return O[0] == self.coordX, O[1] == self.coordY, O[2] == self.coordZ

    def distance(self, d):
        return math.sqrt(((d[0] - self.coordX) ** 2) + ((d[1] - self.coordY) ** 2) + ((d[2] - self.coordZ) ** 2))

    def showInfo(self):
        print("X=",self.coordX, "Y=",self.coordY, "Z=",self.coordZ)



