def time_converter(number):
    hours = 0
    minutes = 0

    while number >= 60:
        hours += 1
        number -= 60

    minutes = number

    if hours == 1 and minutes == 1:
        return f"{hours} hour, {minutes} minute"
    elif hours > 1 and minutes == 1:
        return f"{hours} hours, {minutes} minute"
    elif hours == 1 and minutes > 1:
        return f"{hours} hour, {minutes} minutes"
    elif hours > 1 and minutes > 1:
        return f"{hours} hours, {minutes} minutes"


def main():
    print(time_converter(135))


if __name__ == "__main__":
    main()
