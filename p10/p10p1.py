#prompt user input
#set count and number to zero
#while num is smaller than user input
    #if num square is equal to user input
    #print out result
    #stop
    #else
        # num increment by 1
# if num is greater than user input
    # print result
user_input = int(input('Enter a integer:'))
count = 0
num = 0 
while num <= user_input:
    if num ** 2 == user_input:
        print('Square root of',user_input,'is',num)
        break
    else:   
        num+=1
if num > user_input:
    print('Number is not a perfect square') 
