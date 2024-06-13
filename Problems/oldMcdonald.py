# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_mcdonald(text):
    if len(text)>3:
        return text[:3].capitalize() + text[3:].capitalize()
    else:
        return 'given name is too short'
    
check = old_mcdonald('hariharan')

print(check)
