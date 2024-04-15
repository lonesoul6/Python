""" Declare your age as integer variable """

age = 24;

""" Declare your height as a float variable """

float =  168.5;

""" Declare a variable that store a complex number """
complex = 1+2j;

#Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
#Calculate the perimeter of the triangle (perimeter = a + b + c).
print('Enter side A:')
sideA = input()
a = int (sideA)
print('Enter side B:')
sideB = input()
b = int(sideB)
print('Enter side C:')
sideC = input()
c= int(sideC)

print("Perimeter of the Triangle is: ",a+b+c)

""" Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width)) """

print('Enter the Length:')
Length = input()
l=int(Length)
print('Enter the Breadth:')
Breadth = input()
b=int(Breadth)
print('Area of the Rectangle is: ',l*b)
print('Perimeter of the Rectangle is: ',2*(l+b))