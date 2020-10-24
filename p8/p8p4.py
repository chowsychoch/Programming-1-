#prompt user for input
#declare variable as zero to store the values for different ranges
#while input is greater than zero
 #if input is equal to zero
 #store it 
 #else if  input is between the range of 20 and greater than zero
 #store it in second variable and repeat for the remaining ranges 
 #at the end, prompt for user input again
#if user input is smaller than zero
#print out teh result and done

user_input = int(input('Enter a positive number:'))
sum_zero,sum_20,sum_40,sum_60,sum_80,sum_100,sum_101 =0,0,0,0,0,0,0

while user_input >= 0:
    if user_input == 0:
        sum_zero +=1
    elif 0 < user_input <=20:
        sum_20 +=1
    elif 20 < user_input <=40:
        sum_40 +=1 
    elif 40 < user_input <=60:
        sum_60 +=1
    elif 60 < user_input <=80:
        sum_80 +=1 
    elif 80 < user_input <=100:
        sum_100+=1
    else:
        sum_101+=1
    
    user_input = int(input('Enter a positive number:'))

if user_input < 0:
    print('Number is equal to 0',sum_zero,
          'Number is greater than 0 and less than or equal to 20',sum_20,
          'Number is greater than 20 and less than or equal to 40',sum_40,
          'Number is greater than 40 and less than or equal to 60',sum_60,
          'Number is greater than 60 and less than or equal to 80',sum_80,
          'Number is greater than 80 and less than or equal to 100',sum_100,
          'Number is greater than 100',sum_101, sep="\n"
          )