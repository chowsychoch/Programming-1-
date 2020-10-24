# Function that adds 1 to its argument and sum and prints it out
#declare variable outside the loop
def f(x):
    """Function that adds 1 to its argument and sum and prints it out""" 
    print('In function f:')
    x += 1
    y=1
    sum = x + y
    print('x is', x)
    print('y is', y)
    print('z is', z)
    print('sum,',sum)
    return 

x, y, z, sum = 5, 10, 15, 0

print('Before function f:')
print('x is', x)
print('y is', y)
print('z is', z)

sum = f(x)

print('After function f:')
print('x is', x)
print('y is', y)
print('z is', z)
print('sum is', sum)