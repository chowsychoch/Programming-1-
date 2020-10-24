# Write a password checking program to keep track of how many times a user has entered their password
# incorrectly. 
# Store a password in your program. If the user enters the password incorrectly more than
# three times, 
# print “You have been denied access.” 
# and terminate the program. 
# If the password is
# correct, print “You have successfully logged in.” and terminate the program.
 

count = 0 
password = 'UCD'
while count < 3:
    user_input = input('Enter your password:')
    if (user_input != password):
        print('Not correct. Please try again.')
        count= count +1
    else:
        print('You have successfully logged in.')
        break

if count == 3:
    print('You have been denied access.')
