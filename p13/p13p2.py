# Program to print out the smallest of two numbers entered by the user
# Uses a function min
# if argument one is greater than two
    #return argument 2 
    #else
    #return argument one

def min(a,b):
    """Function that return the smallest of its two argument"""
    if a > b:
        return b
    else:
        return a

# Prompt the user for two numbers
user_input_1  = int(input('Enter two number'))
user_input_2  = int(input('Enter two number'))

print(min(user_input_1,user_input_2))