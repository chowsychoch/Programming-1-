#Pseudocode 
#Function take a parameter
    # if number is equal to one 
        #return two
    # else 
        #return 2 * recur function(nth number - 1 )

def recur_program(number):
    """Function that take a interger and return a function recursively"""
    if number ==1:
        print('Base')
        return 2
    else:
        print('n is', number)
        return 2 * recur_program(number - 1)

#Pseudocode 
#Function that take user input 
#prompt for user input and assign to a variable 
#while input is greater than or equal to one
#print user input and call function in (a)
#if input is smaller than 1 
#throw error

def user_input():
    """Function that prompt user for input"""
    user_num = int(input('Please enter a integer greater than or equal to one:'))
    while user_num >= 1:
        print('number is:',recur_program(user_num))
        user_num = int(input('Please enter a integer greater than or equal to one:'))
    
    if user_num < 1:
        return "Error. It should be greater than or equal to one"
    
print(user_input())