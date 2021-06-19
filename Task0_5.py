#Task 0.5
import math

def area_of_a_triangle(a, b, c):
    parameter = (a + b + c) / 2
    area = math.sqrt((parameter * (parameter - a) * (parameter - b) * (parameter - c)))
    return area

print(area_of_a_triangle(5, 3, 4))