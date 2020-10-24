# Calculating the factorial of a number
# # Program prompts the user for the number
# if number is smaller than zero, print error 
#else set fact to 1 and i to one
#while number is greater than or equal to i 
#fact times i and increment by one
#print out result
number = int(input('Enter the number for which you wish to calculate the factorial (an int >= 0):  '))
if number < 0:
    print('Error:  Number entered was less than 0.')
else:
    fact = 1 
    i = 1
    while number >= i:
        fact*= i
        i += 1
    print('Factorial of', number, 'is', fact)
print('Finished!')    