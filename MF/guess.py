from random import shuffle

lst = ['a','b','c','E']

def shuffled_list(lst):
    shuffle(lst)
    return lst

def player_guess():
    guess=''
    while guess not in ['0','1','2','3']:
        guess = input('Enter in range 0 to 3: ')
    return int(guess)

def check_guess(lst,guess):
    if lst[guess]=='E':
        print('Correct guess!!!!')
    else:
        print('Wrong guess')
        print(lst)

shuffled = shuffled_list(lst.copy())
guess = player_guess()

check_guess(shuffled,guess)