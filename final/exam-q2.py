#prompts the user for a series of strings 
#prompt the user for a file through which it should search

#if file is not found
# open with default file
# else open with the filename with read
# 
# while input is not empty 
# loop over the line of the file
# for user input in line
# read.line  and print out the result
# if not found word, user input should remove the lst index of string and continue to loop until min len of 5 is reached. 


import os
filename = input('Enter a file to operate on (default is lines.txt)')
user_input = input('Enter a string to search for (empty string to exit):')

if not os.path.isfile(filename):
    # print('File not found')
    fh1 = open('lines.txt','r')
else:
    fh1 = open(filename,'r')

while user_input != "":
    for line in fh1:
        # print(line)
        line = line.rstrip()
        if user_input in line:
            print(fh1.readline())
            print('The search string',user_input,'or a prefix of it was found.')
        
        
        elif user_input not in line:
            print('Didn’t find',user_input,'. Now searching for prefixes...')
            
            # for i in range (len(user_input)):
            for i in user_input:
                print(user_input[:-1])
                new_str = user_input[:-1]
                if new_str in line:
                    print(fh1.readline())
                    print('The search string',new_str,'or a prefix of it was found.') 
    user_input = input('Enter a string to search for (empty string to exit):') 

fh1.close()

if user_input =="":
    exit()
    