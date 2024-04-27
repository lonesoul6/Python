myfile = open('myFile.txt')
# # contents = myfile.read()
# contents = myfile.readlines()
# print(contents)
# myfile.close()

# with open('myFile.txt') as new_file:
#     content = new_file.read()
# print(content)
# new_file.close()

with open('create.txt', mode='r+') as filed:
    print(filed.read())