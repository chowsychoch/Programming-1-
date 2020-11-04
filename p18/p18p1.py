def toChars(s):
    """Converts a string to lowercase and removes non-letters
Assumes s is a str.
Converts uppercase letters to lowercase and removes non-letter"""

# First of all, convert uppercase letters to lowercase
    s = s.lower()
# Start with an empty string
    letterstring = '' # Go through s...
    for c in s:
# ... and add the character to the string if it is a letter
        if c in abcdefghijklmnopqrstuvwxyz: 
            letterstring += c
            return letterstring

# iterate each character of index
 # for each character, get the first and last index of character and compare them is equal or not 
    #check the remaining string is smaller than or equal to one
     # if so then return True

def isPal(s):
    """Checks whether the string s is a palindrome using iterative method"""
    for i in range (1,len(s)-1):
        # print(s[i-1], s[-i])
        if len(s) <= 1:
            return True
        if s[i-1] != s[-i]:
            return False
    return True
        

def isPalindrome(s):
    """Checks whether the string s is a palindrome"""
str = input('Enter a string (empty string to exit): ')
while str != '':
    if isPal(str):
        print(str, 'is a palindrome')
    else:
        print(str, 'is not a palindrome')
    str = input('Enter a string (empty string to exit): ')
print('Finished!')
