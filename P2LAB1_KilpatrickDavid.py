# David Kilpatrick
# 10/01/2024
# P2LAB1_KilpatrickDavid
# Circle Formula Calculator

import math

print('What is the radius of the cirle? ', end='')
radius = float(input())
print()

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"The diameter of the circle is  {diameter:.1f}")
print()
print(f"The circumference of the circle is {circumference:.2f}")
print()
print(f"The area of the circle is {area:.3f}")
print()



