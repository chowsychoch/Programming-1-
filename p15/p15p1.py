#Pseudocode 
#Function take a parameter
    # if number is equal to one 
        #return two
    # else 
        #return nth number + recur function(nth number - 1 )

def recur_program(number):
    """Function that take a interger and return a function recursively"""
    print('Number running is ',number)
    if number == 1:
        print('base')
        return 2
    else:
        return ((number + recur_program(number - 1)))
# recur_program(3)

#Pseudocode 
#Function that take user input 
#prompt for user input and assign to a variable 
#while input is greater than or equal to one
#print user input and call function in (a)
#if input is smaller than 1 
#throw error

def user_input():
    user_num = int(input('Enter a number greater than or equal to 1:'))

    while user_num >= 1:
        print(f'user input is {user_num}\n{recur_program(user_num)}')
        return  user_input()

    if (user_num < 1):
        print('Error! It should be greater than or equal to 1')
        return user_num

user_input()