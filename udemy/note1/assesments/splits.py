# Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'

split_words = st.split();
for word in split_words:
    if word.startswith('s')or word.startswith('S'):
        print(word)