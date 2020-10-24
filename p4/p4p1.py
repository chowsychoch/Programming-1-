#Currency Conversion Program 
# Ask the user for an int
hk_dollar_amount = float(input('Enter the amount in HK dollar: '))
print ( 'Amount is ' , hk_dollar_amount)

#Conversion rate HK to Euro
euro_dollar_conversion = 9.1089

euro_amount = hk_dollar_amount / euro_dollar_conversion

print('Today currency in Euro is', euro_amount)
