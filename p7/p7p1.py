# Write a program that prompts the user for a year and checks whether the year is a leap year. Use
# my algorithm from Lecture 8.
# Save this program as p7p1.py.
# 2. Write a program that prompts th


# Prompt the user for a year Read the year
# if year ≥ 0 then
    # if (year mod 4 = 0 and year mod 100 != 0) 
        # or year mod 400 = 0 then
            # Print(“Year is a leap year”)
        # else
            # Print(“Year is not a leap year”)
# else
    # Tell the user that the year must be ≥ 0 Program finishes

# Ask the user to enter a year
year = int(input( 'Enter a year: '))
print('Year entered:', year)

if year >= 0:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: 
        print(year, 'is a leap year. ')
    else:
        print(year, 'is not a leap year.')
else:
    print( 'Year must be greater than 0. ')
    print( 'Finished! ')