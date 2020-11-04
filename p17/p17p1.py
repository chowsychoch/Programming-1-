
# function findDivisors(num1)
# initialise divisors to include one and number
# for i from 2 to half of num1, do
# if num1 mod i == 0 add i to divisors
# return divisors



def findDivisors(num_1):
    """Function that take parameter to find the divisors of a number"""
    divisor = (1,num_1)
    for i in range (2,num_1//2+1):
        if num_1 % i == 0:
            divisor += (i,)
    return divisor
num = int(input('Enter a positive integer: '))
print('Common divsion is:',findDivisors(num))