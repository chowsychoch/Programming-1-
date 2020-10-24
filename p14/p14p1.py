import time
def factorial(x):
    """This is a recursive function to find the factorial of an integer"""
    # print('x is',x)
    if x == 1 or x == 0:
        return 1
    else:
        return (x * factorial(x-1))


print('For recursive Function\n number 10000 factorial is ',factorial(10000))

start_time = time.perf_counter()
end_time = time.perf_counter()
print('recursive Function: ',end_time - start_time)

factorial(10000)

# factorial(10)
# factorial(100) 
factorial(1000000000000000)



def factorial(num):
    count = 1
    fact = 1 
    while count <= num:
        fact= fact * count
        count+=1
    return fact


print('For non-recursive Function\n number 10000 factorial is ',factorial(10000))


start_time = time.perf_counter()
factorial(1000)
end_time = time.perf_counter()
print('non-recursive Function: ',end_time - start_time)

factorial(2000)
factorial(160000)