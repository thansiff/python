from graphics.rectangle import area, perimeter
l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
print("Rectangle area:", area(l, b))
print("Rectangle perimeter:", perimeter(l, b))

import graphics.circle as c
r = int(input("Enter radius: "))
print("Circle area:", c.area(r))
print("Circle perimeter:", c.perimeter(r))

from graphics import *
print("Rectangle area:", rectangle.area(l, b))

from graphics.threeD_graphics import cuboid, sphere
print("Cuboid area:", cuboid.area(2, 3, 4))
print("Cuboid perimeter:", cuboid.perimeter(2, 3, 4))
print("Sphere area:", sphere.area(5))
print("Sphere perimeter:", sphere.perimeter(5))
