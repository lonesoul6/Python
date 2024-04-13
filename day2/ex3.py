""" The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area. """
import math
radius = 30

area= 3.14 * ((radius)**2);
print(area)

a=math.pi * (radius**2)
print(a)

r=input();

rad = int(r);

area_of_circle = math.pi*(rad**2);
circum_of_circle = 2*math.pi*rad;
print(area_of_circle)
print(circum_of_circle)