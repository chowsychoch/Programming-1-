#prompt user for possible number and standard number 
#if possible number is greater than or equal to standard number  or greater than or equal to zero 
# use for range in loop to find the factorial of possible num
# set number as Zero
# if i is zero
# fact increase by 1 
# else if i is 1
# fact increase by 1 
# else fact increase 1 
# loop over the fact - 2 
# each multiply the index
#prompt out input
#repeat the same for k! standard number & (n - k)! 
# to answer = fact_0 // (fact_1 * fact)
#print out result
possible_num = int(input('Enter a possible topping for a pizza:'))
standard_num = int(input('Enter a standard topping for a pizza:'))

if possible_num >= 0 <= standard_num:
    print('You have entered possible topping:', possible_num)
    print('You have entered standard topping:',standard_num)
    for i in range (possible_num):
        fact_0 = 0
        if i == 0:
            fact_0 += 1
        elif i == 1:
            fact_0 += 1 
        else:
            fact_0 += 1
            j=1
            for j in range (1,possible_num +1):
                fact_0 *= j 
                j += 1
    # print('Factorial of', possible_num, 'is', fact_0)
    for i in range (standard_num):
        fact = 0
        if i == 0:
            fact += 1
        elif i == 1:
            fact += 1 
        else:
            fact += 1
            j=1
            for j in range (1,standard_num +1):
                fact *= j 
                j += 1
    # print('Factorial of', standard_num, 'is', fact)
    sum = possible_num - standard_num
    fact_1 = 0
    for i in range (sum):
        
        if i == 0:
            fact_1 += 1
        elif i == 1:
            fact_1 += 1 
        else:
            fact_1 += 1
            j=1
            for j in range (1,standard_num +1):
                fact_1 *= j 
                j += 1
    # print('Factorial of', sum, 'is', fact_1)
    answer = fact_0 // (fact_1 * fact)
print('Total number of different combinations of toppings:',answer)

