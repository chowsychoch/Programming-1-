# Ask the user to enter a password. If the password is correct
#  (ie it matches the password stored in
# the program), print “You have successfully logged in.” 
# and terminate the program. 
# If the password
# is wrong print “Sorry, the password is wrong.” and 
# ask the user to enter the password three times.
# If the user enters the correct password three times, 
# print “You have successfully logged in.” 
# and
# terminate the program; otherwise print “You have been denied access.” 
 

password = 'UCD'
count = 0
user_input = input('Enter your password:')
if count == 0 and user_input == password:
    print('You have successfully logged in.')

else:
    print('Sorry, the password is wrong.')
    count = count + 1 

while count != 0 and count <= 3:
    user_input_again = input('Enter your password again for three times')
    if password == user_input_again:
        count = count + 1
    else:
        print('You have been denied access.')
        break
print('You have successfully logged in.')

