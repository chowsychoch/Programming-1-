# Write a program that prompts the user for an integer and uses a while loop to calculate that
# number of terms of the Fibonacci Series. Try to make the program as small and efficient as
# possible.
# Save this program as p11p2.py.

#prompt user for input 
#set sum to zero and fact and increment to one
#   while user input is greater than increment
#       fact times increment
#       increment by one 
#  print result 
# 
# if user input is smaller than zero
# exit 
# throw erro 
# 
# print finished.   
user_input = int(input('Enter a series of integer:'))

sum = 0 
fact = 1 
i = 1
while user_input >= i:
    fact*= i
    i += 1
print('Factorial of', user_input, 'is', fact)

if user_input < 0:
    exit
    print('Error:  Number entered was less than 0.')

print('Finished!')    