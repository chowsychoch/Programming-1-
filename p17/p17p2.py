
# function findDivisors(num1)
# initialise divisors to include one 
# for i from 2 to minimum number of num1 and num2, do
# if num1 mod i == 0 and num2 mod i == 0 add i to divisors
# return divisors

def findDivisors(num_1,num_2):
    """Function that take parameter to find the divisors of two numbers"""
    divisor = (1,)
    for i in range (2,min(num_1,num_2)+1):
        if num_1 % i == 0 and num_2 % i ==0:
            divisor += (i,)
    return divisor

num1 = int(input('Enter a positive integer: '))
num2 = int(input('Enter a positive integer: '))

print('Common divsion is:',findDivisors(num1, num2))
