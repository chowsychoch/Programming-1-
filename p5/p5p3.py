# Write a program that takes as input a floating-point number and prints out whether the number is positive,
# negative or equal to 0 (Use the if ... elif ... else construct).
# Save this program as p5p3.py.

num = float(input('Enter a number:'))

if num < 0:
    print('Num is negative')
elif num > 0:
    print('Num is positive')
else:
    print('num is 0')