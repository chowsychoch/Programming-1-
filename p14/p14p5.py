# def fibonacci(number):  
#    if number <= 1:  
#        return number  
#    else:  
#        return (fibonacci(number-1 ) + fibonacci(number - 2))  


def fibonacci(number):  
    # print('Number in the scope running:',number)
    if number <= 1:
        # print('number smaller than 1:',number)
        return number  
    else:  
        return (fibonacci(number-1 ) + fibonacci(number - 2))  


#prompt for user input and assign to a variable 
#while input is greater than or equal to zero
#print user input and call function in (a)
#if input is smaller than 0 
#throw error

user_input = int(input('Please enter a positive integer: '))

while user_input >= 0:
    print('Sequence:',user_input)
    for i in range (user_input):
        # print('i',i)
        print('fibonacci is ',fibonacci(i))
    user_input = int(input('Please enter a positive integer: '))

if user_input < 0:
    print('Please give me a positive number i.e. >= 0')
    
