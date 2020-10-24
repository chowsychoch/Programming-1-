# tax calculation 

amount = 202002.25

ratio_1 = 0.6

ratio_2 = 0.4

amount_ratio_1 = amount * ratio_1

print("60% amount",amount_ratio_1)

amount_ratio_2 = amount * ratio_2
print("40% amount",amount_ratio_2)

after_tax_1 = amount_ratio_1 * 13.5 / 100 + amount_ratio_1

after_tax_2 = amount_ratio_2 * 23 /100 + amount_ratio_2

print('For larger amount, initial amount plus taxes:',after_tax_1,'\nFor smaller amount, initial amount plus taxes:',after_tax_2)
