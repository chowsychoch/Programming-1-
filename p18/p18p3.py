#define a Function
#using count function and return the result

def check_userstring(userinput):
    """Function that count the number of code in userinputing"""
    count = 0
    for i in range (len(userinput)):
        # print(i)
        if len(userinput[i:i+4]) == 4:  
            # print(userinput[i:i+2],userinput[i+2],userinput[i+3] )
            # print(len(userinput[i:i+4]))
            if userinput[i:i+2] == 'co' and userinput[i+3] == "e":
                # print(userinput[i+2])
                if userinput[i+2] in 'Dabcdefghijklmnopqrstuvwxyz':
                    count +=1
    return 'Count is ',count

print(check_userstring('codecoDecodecooecopecoe'))

