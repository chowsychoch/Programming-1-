
# Uses a function take argument one
# if arguemnt one is equal to one or argument one equal to zero
#return one
#else
#return argument one times function(argument one - one)

def factorial(x):
    """This is a recursive function to find the factorial of an integer"""
    print('x is',x)
    if x == 1 or x == 0:
        return 1
    else:
        return (x * factorial(x-1))


user_input = int(input('Enter a non-negative number:'))

if user_input < 0:
    print('Error, it should be a non-negative integer')
else:
    print(factorial(user_input))