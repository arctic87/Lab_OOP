import math
from Point_3d import Point3d
from Point_triangle import Triangle

# Создаем 3 точки c координатами x,y,z
p1 = Point3d(1, 2, 4)
p2 = Point3d(5, 10, 15)
p3 = Point3d(3, 6, 9)

# Вычисляем расстояния между этими точками
a = p1.distanceTo(p2)
b = p2.distanceTo(p3)
c = p3.distanceTo(p1)

# Выводим расстояния с 2 знаками после запятой
print("Расстояние a:", "%.2f" % a)
print("Расстояние b:", "%.2f" % b)
print("Расстояние c:", "%.2f" % c)

# Вычисляем площадь треугольника
area = Triangle.computeArea(a, b, c)
print("Площадь треугольника = " "%.2f" % area)
