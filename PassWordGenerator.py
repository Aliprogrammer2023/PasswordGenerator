# my required libraries
import random
import string
import getpass # import the getpass module

# choose your difficulity
level = ''
while level not in ('simple', 'medium', 'high'): # use a while loop to validate the user input
    level = getpass.getpass('Choose your password level(simple,medium,high): ') # use getpass to hide the user input
    if level not in ('simple', 'medium', 'high'):
        print('Invalid level. Please try again.')

#password character numbers
char_num = 0
while char_num <= 0: # use a while loop to validate the user input
    try:
        char_num = int(getpass.getpass('How many characters does your password have? ')) # use getpass to hide the user input
        if char_num <= 0:
            print('Invalid number. Please enter a positive integer.')
    except ValueError: # use a try-except block to catch any exceptions
        print('Invalid input. Please enter a valid number.')

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


