#prompt user input 

num = int(input('Enter the day for which you want to find the date (an integer):'))
print('You entered:',num)

#use the if else to check the number in between and print out the date
if num > 365:
    print('Day number 366 is not in the 2020-2021 academic year!')
elif num >0 and num <= 30:
        print('Day number,' ,num ,'is',num, 'September 2020')
elif num >30 and num <= 61:
        print('Day number,' ,num ,'is',num-30, 'October 2020')
elif num >61 and num <= 91:
        print('Day number,' ,num ,'is',num-61, 'November 2020')
elif num >91 and num <= 122:
        print('Day number,' ,num ,'is',num-91, 'December 2020')
elif num >122 and num <= 153:
        print('Day number,' ,num ,'is',num-122, 'January 2021')
elif num >153 and num <= 181:
        print('Day number,' ,num ,'is',num-153, 'February 2021')
elif num >181 and num <= 212:
        print('Day number,' ,num ,'is',num-181, 'March 2021')
elif num >212 and num <= 242:
        print('Day number,' ,num ,'is',num-212, 'April 2021')
elif num >242 and num <= 273:
        print('Day number,' ,num ,'is',num-242, 'May 2021')
elif num >273 and num <= 303:
        print('Day number,' ,num ,'is',num-273, 'June 2021')
elif num >303 and num <= 334:
        print('Day number,' ,num ,'is',num-303, 'July 2021')
elif num >334 and num <= 365:
        print('Day number,' ,num ,'is',num-334, 'August 2021')

print('Finished')