# Write a program that uses a while loop to prompt the user for a series of numbers,
# check whether each number is divisble by 2, 3, 5 or 7 and print out which of 2, 3, 5 or 7 it is divisible by.
#  Execution of the program continues until a negative number is entered.
# Save this program as p8p1.py.

# prompt user for a number with input method
# print out input
# while number is greater than or zero to zero:
    #divide num by two and store to answer_1 
    #if it is divisible
        #print It is divisible and the number
    #divide num by three and store to answer_2
    #if it is divisible
        #print It is divisible and the number
    #divide num by five and store to answer_3 
        #if it is divisible
        #print It is divisible and the number
    #divide num by seven and store to answer_4 
        #if it is divisible
        #print It is divisible and the number
    # prompt user for input 
# if num is smaller than zero, print it should be greater than zero
# print out done

num = int(input('Enter a non-negative integer:'))
print('You entered:', num)

while num >= 0:
    answer_1 = int(num/ 2)
    # print(num)
    # print(num %2)
    # print(num % 2 != 0)
    if num % 2 != 0:
        print('It is not divisible by 2.',answer_1,'of 2 it is divisible by')
    else:
        print('It is divisible by 2.',answer_1,'of 2 it is divisible by')
    answer_2 = int(num/ 3)
    print(answer_2)
    if num % 3 == 0:
        print('It is divisible by 3.',answer_2,'of 3 it is divisible by')
    else:
        print('It is not divisible by 3.',answer_2,'of 3 it is divisible by')
    answer_3 = int(num/ 5)
    print(answer_3)
    if num % 5 == 0:
        print('It is divisible by 5.',answer_3,'of 5 it is divisible by')
    else:
        print('It is not divisible by 5.',answer_3,'of 5 it is divisible by')
    answer_4 = int(num/ 7)
    print(answer_4)
    if num % 7 == 0:
        print('It is divisible by 7.',answer_4,'of 7 it is divisible by')
    else:
        print('It is not divisible by 7.',answer_4,'of 7 it is divisible by')
    num = int(input('Enter a non-negative integer:'))

if num < 0:
    print('Number entered should be >= 0.')

print('Finished!')

