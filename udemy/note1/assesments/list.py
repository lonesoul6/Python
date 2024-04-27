# Build this list [0,0,0] two separate ways.

# Method 1:
lst = [0,0,0]
# Method 2:
ls = [0]* 3

print(lst)
print(ls)

# Reassign 'hello' in this nested list to say 'goodbye' instead:

list3 = [1,2,[3,4,'hello']]

list3[2][2] = 'goodbye'

print(list3)

# Sort the list below:

list4 = [5,3,4,6,1]
sorted(list4)
list4.sort()
print(list4)