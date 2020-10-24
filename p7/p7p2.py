#  Write a program that prompts the user for a year and checks whether the year is a leap year. Use
# the algorithm on the Wikipedia page (also mentioned in Lecture 8).
# Save this program as p7p2.py.


# if (year is not exactly divisible by 4) then (it is a common year) else
# if (year is not exactly divisible by 100) then (it is a leap year) else
# if (year is not exactly divisible by 400) then (it is a common year) else (it is a leap year)

# Ask the user to enter a year
year = int(input( 'Enter a year: '))
print('Year entered:', year)

if year % 4 !=0:
    print('It is a common year')
elif year % 100 !=0:
    print('It is a leap year')
elif year % 400 != 0:
    print('it is a common year')
else:
    print('it is a leap year')