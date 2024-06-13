# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(text):
    new_text = text.split()
    if new_text[0][0] == new_text[1][0]:
        return True
    else:
        return False
    
check = animal_crackers('Happy foli')

print(check)