##Write a Python function that takes a number in base 10 and a base, both positive ints, 
# and, using the algorithm presented in lectures, returns the number in the base supplied.
# Save this program as p19p1.py.

#function that take two parameter a number in base 10 and a base 
#while number is not <= 0 :
    #remainder = number % base 

def cal_base(quotient,base):
    ans = ""
    while quotient != 0:
        """function to convert base 10 into any base number"""
        remainder = quotient % base 
        # print(quotient)
        quotient = quotient // base 
        # print(f"remainder,{remainder}")
        ans += str(remainder)
        # print(remainder, end="")
        print(ans[::-1])
        
cal_base(39,2)
# cal_base(379,8)


#only work for non-16 base
def cal_base(quotient,base):
    if quotient == 0:
        return ""
    else:
        # remainder = quotient % base
        # quotient = quotient // base
        return str(quotient % base) + cal_base(quotient // base,base)
print(cal_base(2835,16)[::-1])

#work for all base 
def to_string(n,base):
   convert_tString = "0123456789ABCDEF"
   if n < base:
      return convert_tString[n]
   else:
      return to_string(n//base,base) + convert_tString[n % base] 

print(to_string(1280,16))