def findPerfectNum(num):
    """Function that find all the perfect numbers up to and including that number.
"""
    perfect_num = ()
    for i in range (1, num + 1):
        if num % i == 0:
            perfect_num += (i,)
    return perfect_num

# print('Perfect number is:',findPerfectNum(6))


user_input = int(input('Enter a positive integer:'))
print('Perfect number is:',findPerfectNum(user_input))

##Solution found on stackoverflow
##https://www.tutorialgateway.org/python-program-to-find-perfect-number/
n =int(input("Enter any number: "))
perfect_sum = ()
sum=0
for i in range(1, n):
    if(n % i == 0):
        perfect_sum += (i,)
        sum = sum + i
if (sum == n):
    print("The number is a Perfect number!",perfect_sum)
else:
    print("The number is not a Perfect number!")