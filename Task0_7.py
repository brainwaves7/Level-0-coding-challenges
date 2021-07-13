def celsius_to_fahrenheit(degrees_to_convert):
    temperature = (degrees_to_convert * 9 / 5) + 32
    return temperature


print(celsius_to_fahrenheit(25))


def fahrenheit_to_celsius(degrees_to_convert):
    temperature = (degrees_to_convert - 32) / 1.8
    return temperature


print(fahrenheit_to_celsius(77))
