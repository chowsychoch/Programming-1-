#Pseudocode 
#Function take a parameter
    # if number is equal to zero 
        #return 13
    # if number is equal to one
        #return 8     
    # else 
        #return recur function (nth number - 2 ) + 13 times recur function (nth number - 1)
def recur_program(number):
    print('Number running is ',number)
    if number == 0:
        print('base')
        return 13
    elif number == 1:
        return 8
    else:
        return recur_program( number -2 ) + 13 * recur_program(number - 1)
# recur_program(7)

#Pseudocode 
#Function that take user input 
#prompt for user input and assign to a variable 
#while input is greater than or equal to zero
#print user input and call function in (a)
#if input is smaller than 0 
#throw error

def user_input():
    user_num = int(input('Enter a number greater than or equal to 0:'))

    while user_num >= 0:
        print(f'user input is {user_num}\n{recur_program(user_num)}')
        return  user_input()

    if (user_num < 0):
        print('Error! It should be greater than or equal to 0')
        return user_num

user_input()