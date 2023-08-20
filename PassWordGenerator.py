# my required libraries
import random
import string

# choose your difficulity
level = input('Choose your password level(simple,medium,high): ')

#password character numbers
char_num = int(input('How many characters does your password have? '))

#generating password
if level == 'simple':
    try:
        TotalPassWord = ''.join(random.choices(string.digits, k=char_num))
    except:
        print('Sorry! Something went wrong!')

elif level == 'medium':
    try:
        TotalPassWord = ''.join(random.choices(string.ascii_letters, k=char_num))
    except:
        print('Sorry! Something went wrong!')
    
elif level == 'high':
    try:
        TotalPassWord = ''.join(random.choices(string.ascii_letters + string.digits, k=char_num))
    except:
        print('Sorry! Something went wrong!')

#Result    
print(TotalPassWord)
