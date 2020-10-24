#prompt user input for three numbers
#Check the number is not odd number by using mod 2 if yes assign odd num with user input else assign zero to odd num
# repeat for the 2 numbers
#Check the odd num is greater than two other two for 3 numbers 
#if all three odd number is zero, print no odd number found
user_input_1 = int(input('Enter first numbers, please'))
user_input_2 = int(input('Enter the second number:'))
user_input_3 = int(input('Enter the third number:'))

if user_input_1 %2 is not 0:
    odd_num_1 = user_input_1
else:
    odd_num_1 = 0 
if user_input_2 % 2 is not 0:
    odd_num_2 = user_input_2
else:
    odd_num_2 = 0 
if user_input_3 %2 is not 0:
    odd_num_3 = user_input_3
else: 
    odd_num_3 = 0

if odd_num_1 > odd_num_2 and odd_num_1 > odd_num_3:
    print(odd_num_1,'is the largest odd number')
elif odd_num_2 > odd_num_1 and odd_num_2 > odd_num_3:
    print(odd_num_2,'is the largest odd number')
elif odd_num_3 > odd_num_1 and odd_num_3 > odd_num_1:
    print(odd_num_3,'is the largest odd number')
elif odd_num_1 is 0 and odd_num_2 is 0 and odd_num_3 is 0:
    print('none of them is odd number ')