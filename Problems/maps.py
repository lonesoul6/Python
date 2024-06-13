# def square(n):
#     return n**2

my_list =[1,2,3,4,5,6,7,8,9]

# check = list(map(square,my_list))

# print(check)

# for item in map(square,my_list):
#     print(item)

test=list(filter(lambda n : n%2 ==0,my_list))

print(test)