# Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'

first_letter =[word[0]for word in st.split()]
 
print(first_letter)