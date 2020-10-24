# Write a program that uses a while loop to sum the first 5000 integers and prints out the total.
# Save this program as p7p4.py


#initiate number and sum as zero
# while count is smaller than 5000 
# start to add sum with number of count
#plus 1 for count number and continue till it end 
count = 0 
sum = 0 

while count < 5000:
    sum = sum + count
    print(sum,'\n')
    count= count + 1 