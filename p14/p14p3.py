#For number in range start from 2 to 20
    #for number in range start from 2 to number
        # if number is divisible by number
        # print result
        # break
    #else:
    # printout this is a prime number 


for number in range(2, 20):
    print('number',number)
    for i in range(2, number):
        print('i',i) 
        if number % i == 0:
            print(number, "equals", i, "*", number//i)
            break
        #stop right now
    else:
        # loop fell through without finding a factor
        print(number, "is a prime number")
print("Finished!")
