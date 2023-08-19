# my required libraries
import random
import string

E_num=[]
E_char=[]
E_comp=[]
# Functions
def random_number():
    return random.randint(0,9)

def random_char():
    return random.choice(string.ascii_letters)

# choose your difficulity
level=input('Choose your password level(simple,medium,high): ')

#password character numbers
char_num=int(input('How many characters does your password have? '))

#generating password
if level=='simple':
    try:
        for y in range(0,char_num):
            num1=str(random_number())
            E_num.append(num1)
        TotalPassWord=''.join(E_num)
    except:
        print('Sorry! Something went wrong!')

elif level=='medium':
    try:
        for o in range(0,char_num):
            char1=random_char()
            E_char.append(char1)
        TotalPassWord=''.join(E_char)
    except:
        print('Sorry! Something went wrong!')
    
elif level=='high':
    try:
        for w in range(0,char_num):
            num2=str(random_number())
            char2=random_char()
            chosen=random.choice([num2,char2])
            E_comp.append(chosen)
            TotalPassWord=''.join(E_comp)
    except:
        print('Sorry! Something went wrong!')

#Result    
print(TotalPassWord)