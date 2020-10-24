#prompt user input
# count set to zero and sum set to zero
#while count is smaller than user input 
#sum+count
#count increment by one
#print teh result 

user_input = int(input('Enter a positive integer'))
if user_input < 0:
    print('Please enter a positive integer')
else:
    count = 0 
    sum = 0
    while count <= user_input:
        sum +=count
        count+=1
print(sum)   
