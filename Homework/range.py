# a function that checks whether a number is in a given range (inclusive of high and low)

def range_check(a,b,c):
    if a in range(b,c):
        return f'{a} is in range of {b} and {c}'
    else:
        return f'{a} not in range of {b} and {c}'
    

check = range_check(1,2,99)

print(check)