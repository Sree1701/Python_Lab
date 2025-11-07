from graphics import rectangle, circle
from graphics._3D_graphics import cuboid, square

print("Rectangle Area:", rectangle.area(5,3), "Rectangle Perimeter:", rectangle.perimeter(5,3))
print("Circle Area:", circle.area(4), "Circle Perimeter:", circle.perimeter(4))
print("Cuboid Surface Area:", cuboid.surface_area(2,3,4), "Cuboid Volume:", cuboid.volume(2,3,4))
print("Square Area:", square.area(6), "Square Perimeter:", square.perimeter(6))

