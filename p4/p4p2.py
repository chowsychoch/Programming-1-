import math
#
length = float(input('Enter a length, please~'))
print('Your input length is', length)

#The area of a square with side of that length
area_of_square = length ** 2 
print('area_of_square:',area_of_square)

#The volume of a cube with side of that length

volume = length ** 3 
print('volume:',volume)

#The area of a circle with diameter of that length
radius = length / 2 
area_of_circle = math.pi * radius **2

print('area_of_circle:',area_of_circle)

#The volume of a sphere with diameter of that length

volume_of_sphere = math.pi * radius ** 3 

print('volume_of_sphere:',volume_of_sphere)

#The volume of a cylinder with diameter of that length and side of that length

volume_of_cylinder = length * math.pi * radius ** 2 

print('volume_of_cylinder:',volume_of_cylinder)
