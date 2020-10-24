# prompt user for a number with input method
num = int(input('Enter a non-negative integer:'))
# print out input
print('You entered:',num)
#Set the count as zero
count = 0
# if num is smaller than zero, print it should be greater than zero
if num < 0:
    print('Number entered should be >= 0.')
else:
    #else set the count limit to 1 to use while loop to loop over 
    while count<1:
        #divide num by three, print out answer and so on. 
        answer_1 = num//3
        print('Number of numbers divisible by 3:', answer_1)
        answer_2 = num // 5
        print('Number of numbers divisible by 5:',answer_2)
        answer_3 = num // 7
        print('Number of numbers divisible by 5:',answer_3)
        answer_4 = num // 11
        print('Number of numbers divisible by 5:',answer_4)
        count = count + 1
#print out done  
print('Finished!')



