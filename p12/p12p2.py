# (a) Write a function that takes as its argument a non-negative integer 
# and prints out that number of terms of the Fibonacci Series. 
# This function should not return an explicit value.

def fibonacci(number):
     #fib idex 0 , 1 mut be 1 
    f_0, f_1 = 0 , 1
    i = 0 
    if number == 0:
        print(f_0) 
    if number == 1:
        print(f_0)
   
    else:
        while i < number:
            print(f_0)
            fib = f_0 + f_1 
            # print('fib',fib)
            #reassign
            f_0 = f_1 
            f_1 = fib 
            i += 1 

# fibonacci(0)
# fibonacci(1)
# fibonacci(7)

# (b) Write a program that prompts the user for an integer and 
# checks that the number entered is non-negative. 
# If it is, it calls the function defined in part (a); 
# if not, it prints out an appropriate error message.
# Save this program as p12p2.py.

user_input = int(input('Enter a non-negative number:'))

if (user_input < 0):
    print('Error! It should be non-negative number')
else:
    fibonacci(user_input)

