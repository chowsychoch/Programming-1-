# Write a program that takes as input an integer and prints out one of the following messages indicating whether
# the number is in one of the specified ranges:
# • Number is equal to 0
# • Number is greater than 0 and less than or equal to 20
# • Number is greater than 20 and less than or equal to 40
# • Number is greater than 40 and less than or equal to 60
# • Number is greater than 60 and less than or equal to 80
# • Number is greater than 80 and less than or equal to 100
# • Number is greater than 100
# If the number entered is less than 0, a message should be printed out to that effect.
# Save this program as p5p4.py.

num = int(input('Enter a num'))
if num == 0:
    print('Num is 0')
elif num > 0 and num <=20:
    print('Number is greater than 0 and less than or equal to 20')
elif num > 20 and num <=40:
    print('Number is greater than 20 and less than or equal to 40')
elif num > 40 and num <=60:
    print('Number is greater than 40 and less than or equal to 60')
elif num > 60 and num <=80:
    print('Number is greater than 60 and less than or equal to 80')
elif num > 80 and num <=100:
    print('Number is greater than 80 and less than or equal to 100')
elif num > 100:
    print('Number is greater than 100')
else:
    print('Number entered is less than 0')
        