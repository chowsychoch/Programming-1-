# Write a program that uses a while loop to go through the first 50 integers and prints out each
# number and the square of the number.
# Save this program as p7p3.py.

#initiate the number and the count number as zero
#while count is smaller than 50
#print out number and square of number, then add one for both count and number
n = 1
count = 0 

while count < 50: 
    print('Number:',n, 'Square of number:', n **2 )
    n+=1
    count = count + 1
