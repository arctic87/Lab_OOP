# -*- coding: utf-8 -*-
import math

class Triangle:
    #статический метод для расчета площади треугольника (Формула Герона)
    @staticmethod
    def computeArea(a, b, c):
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return area
