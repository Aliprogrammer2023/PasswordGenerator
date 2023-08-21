# my required libraries
import random
import string
import getpass # import the getpass module

# choose your difficulity
level = getpass.getpass('Choose your password level(simple,medium,high): ') # use getpass to hide the user input

#password character numbers
char_num = int(getpass.getpass('How many characters does your password have? ')) # use getpass to hide the user input

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

