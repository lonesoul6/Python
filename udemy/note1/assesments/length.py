# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'

words = list(st.split())
print(words)

for word in words:
    if len(word)%2 ==0:
        print(word,' is even')
        