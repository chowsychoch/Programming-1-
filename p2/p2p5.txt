# #slicing
animal ='herdofelephants'
seg=animal[2:2]
#(a) What happens when x and y are the same?
print('Segment a is:', seg)
#it print out nothing

# (b) What happens when x is greater than y?
seg2=animal[4:2]
print('Segment b is:', seg2)
#it prints out nothing

# (c) What happens when x is omitted?
seg3=animal[:2]
print('Segment c is:', seg3)
#it prints out he
# (d) What happens when y is omitted?
seg4=animal[3:]
print('Segment d is:', seg4)
#Segment d is: dofelephants

# (e) What happens when both x and y are omitted?
seg5=animal[:]
print('Segment e is:', seg5)
#Segment e is: herdofelephants
