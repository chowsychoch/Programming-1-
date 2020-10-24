# Write a program that prompts the user for a series of integers and, for each of the numbers
# entered, uses a for loop to calculate that number of terms of the Fibonacci Series. The
# program should stop when a negative number is entered.
# Save this program as p11p3.py.


#prompt user for input 
#set sum to zero 
#while user input is greater than zero 
#set fact and increment to one
#   while user input is greater than or equal than increment
#       fact times increment
#       increment by one 
#  print result 
#   sum increases the fact 
# if user input is smaller than zero
# exit 
# throw error 
# 
# print finished.  
user_input = int(input('Enter a series of integer:'))

sum = 0 
while user_input>0:
    fact = 1 
    i = 1
    while user_input >= i:
        fact*= i
        i += 1
    print('Factorial of', user_input, 'is', fact)
    sum+=fact
    print('Finished!',sum)
    user_input = int(input('Enter a series of integer:'))

if user_input < 0:
    exit
    print('Error:  Number entered was less than 0.')

print('Finished!')    