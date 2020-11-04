#define function take one variable 
#assume check is False 
#iterate the length of string
# check string of index i to 3 is equal to xyz
    #if yes ,  check the index before i is '.'
    #check is True
    #return check
#return check 


def check_xyz(string):
    check = False 
    """function that takes a string as an argument and returns True if the given string
contains an appearance of “xyz” where the “xyz” is not directly preceeded by a period (“.”)"""
    for i in range (len(string)):
        if string[i:i+3] == "xyz":
            if string[i-1] != '.':
                check = True
                return check
            return check


print(check_xyz('abcdef.xyz'))
print(check_xyz('xyz.xyz'))
print(check_xyz('x.xyz'))