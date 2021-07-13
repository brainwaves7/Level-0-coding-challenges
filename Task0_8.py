def time_converter(number):
    hours = 0
    minutes = 0

    while number >= 60:
        hours += 1
        number -= 60

    minutes = number

    if hours == 1 and minutes == 1:
        print(f"{hours} hour, {minutes} minute")
    elif hours > 1 and minutes == 1:
        print(f"{hours} hours, {minutes} minute")
    elif hours == 1 and minutes > 1:
        print(f"{hours} hour, {minutes} minutes")
    elif hours > 1 and minutes > 1:
        print(f"{hours} hours, {minutes} minutes")
    else:
        print("Have a great day")


time_converter(71)
time_converter(133)
