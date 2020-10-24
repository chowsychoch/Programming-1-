Write a program that prompts the user for a series of integers and, for each of the numbers
entered, performs exhaustive enumeration to find the integer cube root of the number.
If the number is not a perfect cube, the program should print out a message to that effect.
Note that the program should work for negative numbers as well as positive numbers. The
program should exit when a 0 is entered.
Save this program as p10p2.py

# Finding the integer cube root of a number
# Program prompts the user for the number
#while number is not equal to zero
    #if number is smaller than zero
    # assign with - in number and store it in new number
    # else
    #   store it in new number
    # set root as zero
    # while cube **3 is smaller than new number
    #   increment by one for root 
    # 
    # if cube root **3 is equal to new number
    #       if number is smaller than zero
    #           assign  - to cube root
    #           print out result
    # else  
    #       print out result
    # prompt for user input 
# finished 
# if number is qeual to aero 
# exit 
number = int(input('Enter the number for which you wish to calculate the cube root:  '))


while number !=0:
    if number < 0:
        new_number = -number
        print('new_number:',new_number)
    else:
        new_number = number
    cube_root = 0
    while cube_root**3 < new_number:
        print(cube_root)
        cube_root += 1 
    print('End',cube_root)
    if cube_root**3 == new_number:
        if number < 0:
            cube_root = -cube_root
        print('Cube root of', number, 'is', cube_root)
    else:
        print(number, 'is not a perfect cube.')
    number = int(input('Enter the number for which you wish to calculate the cube root:  '))

print('Finished!')

if number == 0:
    exit
else: