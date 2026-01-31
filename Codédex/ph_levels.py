'''A lot of the times inside conditions, we are comparing two values. To do so, we need to use a different type of operators called relational operators that compares values:

== equal to
!= not equal to
> greater than
< less than
>= greater than or equal to
<= less than or equal to'''

ph = int(input('Type the level pH between 0 and 14: '))

if ph <0 or ph > 14:
    print('You have to enter a number between 0 and 14')
elif ph == 0 or ph <= 6:
    print('You have a Acidic pH')
elif ph == 7:
    print('You have a Neutral pH')
elif ph == 14 or ph >= 8:
    print('You have a Basic pH')

#Answer than the page accept
'''if ph > 7:
    print('Your pH is Basic')
elif ph < 7:
    print('Your pH is Acidic')
else:
    print('Your pH is Neutral')'''