#Even numbers are divisible by 2 and the remainder is zero.
# How do you check if a number is even or not using python?

n = input("Enter your Number:  ");
num=int(n)

if num%2!=0:
    print(num,' is odd')
else:
    print( num, ' is even')