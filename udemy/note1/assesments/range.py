# Use range() to print all the even numbers from 0 to 10.
even = [x for x in range(0,11) if x%2==0]
print(even)

for num in range(0,11):
    if num%2 ==0:
        print(num)