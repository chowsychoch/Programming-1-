# Set the range between 1 and 10000. 
# if number is divided my 3 or 5 
#print sum of dividable number 


for  i in range (1,10000):
    print('number', i)
    if i % 3 == 0 or i % 5 == 0:
        total = i / 3 + i / 5 
        print('Total:', int(total)) 