# Calculating the factorial of a number
# Program prompts the user for the number
# Prompt the user for a number
# if numbersmaller than zero, print Error
# else for loop  of number 
# set number as Zero
# if i is zero
# fact increase by 1 
# else if i is 1
# fact increase by 1 
# else fact increase 1 
# loop over the fact - 2 
# each multiply the index
# print out result

number = int(input('Enter the number for which you wish to calculate the factorial (an int >= 0):' ))

if number < 0:
    print('Error: Number entered was less than 0.')
for i in range (number):
    fact = 0
    if i == 0:
        fact += 1
    elif i == 1:
        fact += 1 
    else:
        fact += 1
        j=1
        for j in range (1,number +1):
            fact *= j 
            j += 1
print('Factorial of', number, 'is', fact)
print('Finished!')