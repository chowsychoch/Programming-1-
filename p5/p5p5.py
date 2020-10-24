# . Write a program that takes as input a string and checks whether the string entered is the name of a town
# or city known to the program. The towns and cities should include: Dublin, Belfast, Cork, Limerick, Derry,
# Galway, Lisburn, Kilkenny, Waterford and Sligo. If the name of one of these towns or cities is entered, the
# program should print out the string “”, where x is the name of the town or city and
# y is the province (Ulster, Munster, Leinster or Connacht) in which the town or city is situated. If the string
# entered is not recognised, the message “Sorry, I didn’t recognise that name.” should be printed out.
# Save this program as p5p5.py.

user_input = input('Please enter a town/city:')

if user_input == 'Dublin':
    print('You entered is',user_input,user_input,'is the name of town',user_input,'is in Leinster')
elif user_input == 'Belfast':
    print('You entered is',user_input,user_input,'is the name of town',user_input,'is in Ulster')
elif user_input == 'Cork':
    print('You entered is',user_input,user_input,'is the name of town',user_input,'is in Munster')
elif user_input == 'Limerick':
    print('You entered is',user_input,user_input,'is the name of town.',user_input,'is in Munster')
elif user_input == 'Derry':
    print('You entered is',user_input,user_input,'is the name of town.',user_input,'is in Leinster')
elif user_input == 'Galway':
    print('You entered is',user_input,user_input,'is the name of town.',user_input,'is in Connacht')
elif user_input == 'Lisburn':
    print('You entered is',user_input,user_input,'is the name of town.',user_input,'is in Ulster')
elif user_input == 'Kilkenny':
    print('You entered is',user_input,user_input,'is the name of town.',user_input,'is in Leinster')
elif user_input == 'Waterford':
    print('You entered is',user_input,user_input,'is the name of town.',user_input,'is in Munster')  
elif user_input == 'Sligo':
    print('You entered is',user_input,user_input,'is the name of town.',user_input,'is in Connacht')  
else:
    print('Sorry, I didn’t recognise that name.')
# towns = ['Dublin', 'Belfast', 'Cork', 'Limerick', 'Derry','Galway', 'Lisburn', 'Kilkenny', 'Waterford', 'Sligo']

# for town in towns:
#     if user_input == town:
#         print('You entered is'town,town,'is in')


