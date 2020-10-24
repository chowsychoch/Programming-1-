# Write a program that takes as input an amount of currency (a float) and an exchange rate to another currency (a float) and prints out the value of the original amount in the other currency. 
# For the exchange rate, pick two currencies and use today’s exchange rate.
# When the currency amount is entered by the user, the program should check that the amount is non-negative. 
# If the amount is negative, the message “Amount must be >= 0. 
# Please try again.” should be printed out and the program should exit.
# Save this program as p4-5p1.py.

#Ask for user's input 
hk_dollar_amount = float(input('Enter the amount in HK dollar: '))
print ( 'Amount in HK dollar ' , hk_dollar_amount)

#Conversion rate HK to Euro
euro_dollar_conversion = 9.1089

if hk_dollar_amount >=0:
    print('Amount in euro is:',hk_dollar_amount / euro_dollar_conversion)
else:
    print('Amount must be >= 0. Please try again')


