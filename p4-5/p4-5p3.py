# Write a program that takes as input an amount of income(a float),
# divides the amount in the ratio 60: 40,
# calculates the tax due according to two different tax rates(23 % on the larger amount and 41 % on the smaller),
# and prints out the initial amount, the two different tax amounts, the total tax and the total nett income
# (initial amount less taxes).
# When the amount is entered by the user,
# the program should check that it is non-negative.

# If the amount of income is negative, the message “Amount of income must be >= 0. Please try again.”
# should be printed out and the program should exit.


# tax calculation
amount_in_total = float(input('Enter the taxable amount:'))
if amount_in_total < 0:
    print('Your input amount is', amount_in_total)
else:
    ratio_1 = 0.6
    ratio_2 = 0.4
    amount_ratio_1 = amount_in_total * ratio_1
    print("60% amount", amount_ratio_1)
    amount_ratio_2 = amount_in_total * ratio_2
    print("40% amount", amount_ratio_2)

    tax_amount_23 = amount_ratio_1 * 23 / 100 
    tax_amount_41 = amount_ratio_2 * 41 / 100 

    after_tax_1 = amount_ratio_1 - tax_amount_23
    after_tax_2 = amount_ratio_2 - tax_amount_41
    print('For larger amount, the initial amount:', amount_ratio_1,'tax amount:',tax_amount_23,
      '\nFor smaller amount, initial amount:', amount_ratio_2,'tax amount:',tax_amount_41,'the total tax:',tax_amount_23+tax_amount_41,'total nett income:',amount_ratio_1+amount_ratio_2-(tax_amount_23+tax_amount_41))
