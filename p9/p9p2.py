#prompt user for positive integer
#set count and sum to zero
#while input is greater than zero
#while count is smaller than or equal to input, increment count by one and sum by count
# print the sum 
#reset userinput, count, sum to zero 
#prompt user input 
#if input is smaller than zero
#print out total and prompt for alert 
user_input = int(input('Enter a positive integer'))
count = 0 
sum = 0

while user_input > 0:
    while count <= user_input:
        sum +=count
        count+=1
    print(sum)
    user_input = 0 
    count = 0
    sum = 0
    user_input = int(input('Enter a positive integer'))  

if user_input < 0:
    print('Please enter a positive integer')