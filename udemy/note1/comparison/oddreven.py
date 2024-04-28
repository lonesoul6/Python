# odd or even using for loop

num = input("Enter the number: ")

for check in num:
    check = int(num)
    if check % 2 == 0:
        print("Even number: ",num)
    else:
        print("Odd number: ",num)