# (a) Write a function that takes as its single argument a non-negative integer 
# and returns the factorial of the number.

#function take 1 argument
#initiate count and fact 
#while count is smaller than input
#fact times count and increment count by one
#return fact 

def factorial(num):
    count = 1
    fact = 1 
    while count <= num:
        fact= fact * count
        count+=1
        # print(fact)
    return fact

# print(factorial(5))



# (b) Write a program that prompts the user for an integer 
# and checks that the number entered is non-negative. 
# If it is, it calls the function defined in part (a) 
# and prints out the result; if not, it prints out an appropriate error message.

#prompt user for input
#if input is smaller than 0:
    #print error msg
#else:
    #call function factorial
user_input = int(input('Enter a non-negative integer:'))

if user_input < 0:
    print('Error! it should be a non-negative number!')
else:
    # factorial(user_input)
    print(factorial(user_input))