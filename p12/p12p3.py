def square_root(number):
    epsilon = 0.01
    step = epsilon ** 2
    root = 0.0
    while abs( number - root ** 2) >= epsilon and root ** 2 <= number:
        root +=step 
    if abs(number - root**2) < epsilon:
        print('root', root)
        return root
    else:
        print('Failed', number)


# square_root(1000)

# (b) Write a program that prompts the user for
#  a floating-point number and checks that the number 
#  entered is non-negative. If it is, it calls the function defined
#   in part (a) with the number and a tolerance defined in the program 
#   and prints out the square root of the number; if not, 
#   it prints out an appropriate error message.
# Save this program as p12p3.py.


user_input = float(input('Enter a float number i.e. number with decimal:'))

if user_input < 0:
    print('Error')
else: 
    square_root(user_input)

