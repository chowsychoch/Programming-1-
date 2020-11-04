#Prompt user for input 
# initiate i to loop over 
    # if str[i: i+2] == cat 
        #increment count by one 
    #elif  str[i: i+2] == dog
     #increment count dog by one 
#return count of cat and dog


def findString(user_input):
    """Function that calculate the number of string"""
    count_cat,count_dog = 0,0
    for i in range (len(user_input)-1):
        if user_input[i:i+3] == "cat":
            count_cat += 1
        elif user_input[i:i+3] == "dog":
            count_dog += 1
    print(f'Number of cat in string:{count_cat}.\nNumber of dog in string:{count_dog}.')

user_input = input('Please give me a string:')
findString(user_input)