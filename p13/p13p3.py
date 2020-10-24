# Implement the program that uses the print max function from the lectures 
# (Page 9 of the notes on Lecture 15, the section on “Functions within functions”). 
# Ensure that you understand what is going on and how it works.
# Save this program as p13p3.py.


# Uses a function min
# if argument one is greater than two
    #return argument 2 
    #else
    #return argument one

def max(a,b):
    """function take two argument of a and b and retrun the largest number"""
    if a > b:
        return a 
    else:
        return b

# Program to print out the largest of two numbers entered by the user
def print_max():
    """Function that print out the result of function max"""
    print(max(1,2))
    return

print(print_max)