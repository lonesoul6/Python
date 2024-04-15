""" Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14. """
import math
radius = int(input("enter the Radius of the Circle: "))

area = math.pi * (radius**2)
circumference = 2 * math.pi * radius;

print('Area of the circle is:',area)
print('Circumference of the circle is:',circumference)


