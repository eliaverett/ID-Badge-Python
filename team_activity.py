import math
square = float(input("What is the length of a side of the square?\n"))
area_square = square ** 2
print(f'The area of the square is {area_square}')
print()

length_rec = float(input("What is the length of the rectangle?\n"))
width_rec = float(input("What is the width of the rectangle?\n"))
area_rec = length_rec * width_rec
print(f'The area of the rectangle is {area_rec}')
print()

radius_circle = float(input("What is the radius of the circle?\n"))
area_circle = radius_circle * math.pi
print(f'The area of the circle is {area_circle}')
print()
