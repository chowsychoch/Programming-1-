#prompt user for int
#print out input
# if user input < 0:
    #print out error 
# set number as one 
#while num is smaller or equal to input
    #set index to one 
    #while  index is smaller than user input
    #print out index * num 
    #increment by one
#print space line 
# num increment by one 
# print finished 

user_input = int(input('Enter a positive number:'))
print('You entered:',user_input)
if user_input < 0:
    print('You have to enter a positive number')

num = 1

while num <= user_input:
    idx = 1
    while idx <= user_input:
        print(idx*num, end=" ")  
        idx = idx + 1
    print()
    num  = num + 1


print('Finished')

        
