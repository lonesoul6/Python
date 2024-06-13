# MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(text):
    return ' '.join(text.split()[::-1])

check = master_yoda('I am Python')

print(check)