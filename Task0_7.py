#Task 0.7
degrees = 0
def celsius_to_fahrenheit(deg) :
    degrees = (deg * 9 / 5) + 32
    return degrees

print(celsius_to_fahrenheit(25)) 

def fahrenheit_to_celsius(num) :
    degrees = (num - 32) / 1.8
    return degrees

print(fahrenheit_to_celsius(77))
