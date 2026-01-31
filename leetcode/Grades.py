# Watching about conditionals statements, if, else, True and False

import random

for i in range(5):
    grade = random.randint(0,100)
    if grade >= 55:
        print(f'You have {grade}')
        print('You passed, congrats!!')
    else:
        print(f'You have {grade}')
        print('You failed, better luck next time.')