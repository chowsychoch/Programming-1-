#function to take a parameter with string and digit
#initiate ans as zero 
#loop over the range of length of string 
#with each index use the base 16 to find the value of index times 16 of power index
#incerase the answer
#return value
def convert_base10(str_num):
    """Function to convert base 16 number into base 10 number """
    ans = 0
    for i in range (0,len(str_num)):
        # print('index',i)
        # print('sum',str_num[-i-1])
        ans += int(str_num[-i-1],16) * 16 **i
        # print(ans)
    return ans


print(convert_base10('9B3'))
