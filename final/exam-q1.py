#prompt user for string 
#while user input > 0 
#put empty string as variable 
#for each charc of string input
#check if each char is in the letter digit and space and stor it in a variable 
#reverse the string and compare it 
#if yes print true if not print false
user_input = input('Enter a string (empty string to exit):')

while user_input != "":
    #do sth 
    letterstring = ''
    for i in user_input:
        if i in "abcdefghijklmnopqrstuvwxyz0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            letterstring += i
            # print(letterstring)
    r_string = letterstring[::-1]

    if letterstring == r_string:
        print(user_input,'is a palindrome.')
    else:
        print(user_input,'is not a palindrome.')

    #ask again for string
    user_input = input('Enter a string (empty string to exit):')


if user_input == "":
    exit()

print('Finished')
