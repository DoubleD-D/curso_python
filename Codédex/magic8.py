#Learning about modules and how to import.
#In this case we use the random module to do a little example.

import random

#Example
#for i in range(10):
#    num = random.randint(1, 9)
#    print(num)


#Do a program that respond to any Yes or No questions with a different answer each time it executes

question = input('Do some question to Magic 8 ball: ')

answer = random.randint(1, 9)

if answer == 1:
    print('Yes - definitely.')
elif answer == 2:
    print('It is decidedly so.')
elif answer == 3:
    print('Without a doubt.')
elif answer == 4:
    print('Reply hazy, try again.')
elif answer == 5:
    print('Ask again later.')
elif answer == 6:
    print('Better not tell you now.')
elif answer == 7:
    print('My sources say no.')
elif answer == 8:
    print('Outlook not so good.')
else:
    print('Very doubtful.')

