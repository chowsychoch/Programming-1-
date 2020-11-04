Write a program that prompts the user for a series of strings and counts and prints out the
number of vowels (letters ’a’, ’e’, ’i’, ’o’ or ’u’) in each string. The program should exit when
an empty string is entered.
Save this program as p10p3.py.

#prompt user input 
#set variable to store five count of vowels
#if user input is empty string
#stop  and exit
#else
    #for each of user input, iterate to check with each is each to specific vowels
#print out result 
user_input = input('prompt user for string input:')
letter_a, letter_e, letter_i, letter_o, letter_u = 0,0,0,0,0

if user_input == "":
    print('End')
    exit
else:
    for i in (user_input):
        if i == "a":
            letter_a +=1
        elif i == "e":
            letter_e +=1
        elif i == "i":
            letter_i +=1
        elif i == "o":
            letter_o +=1
        elif i == "u":
            letter_u +=1

print('a',letter_a,'e',letter_e,'i',letter_i,'o',letter_o,'u',letter_u)

##other solution
s = input('prompt user for string input:')
count = 0
vowels = ['a' , 'e' , 'i' ,'o' , 'u']
for char in s:
    if char in vowels: # check if each char in your string is in your list of vowels
        count += 1
print ('Number of vowels: ' + str(count)) # count is an integer so you need to cast it as a str