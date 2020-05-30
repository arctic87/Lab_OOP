import math
from Point import Point
from Point_3d import Point3d
from Point_triangle import Triangle

#Создаем 2 точки и определяем расстояние между ними
p1 = Point3d(10, 12, 24)
p2 = Point3d(15, 25, 50)
p1.showInfo()
p2.showInfo()
print("Расстояние между точками:", p1.distance(p2.getXYZ()))

#Создаем треугольник и определяем его площадь
t1 = Triangle(10, 12, 24, 15, 25, 50)
t1.showInfo()
print("Площадь заданного треугольника:", t1.area())
