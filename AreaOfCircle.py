#Alex Flores
#November 7, 2023
#Problem 1 AreaOfCircle
# The code returns the area of a circle by using the radius.

import math

r = input('Radius of circle?')
def area_of_circle(r):
    area_of_circle = r * r * math.pi
    return area_of_circle
print(area_of_circle)