def celsius_to_fahrenheit(degrees_to_convert):
    temperature = (degrees_to_convert * 9 / 5) + 32
    return temperature


def fahrenheit_to_celsius(degrees_to_convert):
    temperature = (degrees_to_convert - 32) / 1.8
    return temperature


def main():
    print(celsius_to_fahrenheit(25))
    print(fahrenheit_to_celsius(77))


if __name__ == "__main__":
    main()
