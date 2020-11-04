#define a Function
#using count function and return the result

def check_string(str):
    """Function that count the number of code in string"""
    x = str.count('code')
    return x

print(check_string('CodecodecodecodecodeCode'))



def check_string(str):
    """Function that count the number of code in string"""
    count = 0
    for i in range (len(str)-1):
        # print(str[i:i+4])
        if str[i:i+4] == 'code':
            count +=1  
    return count

print(check_string('CodecodecodecodecodeCode'))