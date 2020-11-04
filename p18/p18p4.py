import re
#import re module
#define function take two variable
#if length of variable one smaller than variable two 
    # use regex to search variable one with variable two 
    #else use regex to search variable two with variable one
 

def check_string(str_one, str_two):
    """function that takes as arguments two strings and returns True if either of the strings
appears at the very end of the other string"""
    str_one = str_one.lower()
    str_two = str_two.lower()
    # print(str_one,str_two)
    if len(str_two) < len(str_one):
        return bool(re.search(str_two+'$',str_one))
    else:
        return bool(re.search(str_one+'$',str_two))

print(check_string('abcabc','abcd'))
print('Finished')