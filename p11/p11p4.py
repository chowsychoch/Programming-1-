#prompt user for input 
#set fact and increment to one
#   while user input is greater than or equal than increment
#       fact times increment
#       increment by one 
#  print result 

#set fact and increment to one
#set 2 times user input 
#   while 2 times user input  is greater than or equal than increment
#       fact times increment
#       increment by one 
#  print result 

#set fact and increment to one
#set user input + 1 
#   while user input + 1 is greater than or equal than increment
#       fact times increment
#       increment by one 
#  print result 
# calculate answer with the formula
# print result 

user_input = int(input('Prompt user for input:'))

# n!
fact = 1 
i = 1
while user_input >= i:
    fact*= i
    i += 1
print('Factorial of', user_input, 'is', fact)

#(2n)!

fact_2n = 1 
i_2n = 1
n_2 = 2 * user_input
while n_2 >= i_2n:
    fact_2n *= i_2n
    i_2n += 1
print('Factorial of', user_input, 'is', fact_2n)

# (n +1)!
fact_n_1 = 1 
i_n_1 = 1
user_input_2 = user_input + 1 
while user_input_2 >= i_n_1:
    fact_n_1*= i_n_1
    i_n_1 += 1
print('Factorial of', user_input, 'is', fact_n_1)

answer = fact_2n / (fact_n_1 * fact)
print(user_input,'Number of Catalan Numbers is',int(answer))