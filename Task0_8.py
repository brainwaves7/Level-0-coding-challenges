def time_converter(number):
    hours = int(number / 60)
    minutes = int(number % 60)

    if hours == 1 and minutes == 1:
        return f"{hours} hour, {minutes} minute"
    elif hours > 1 and minutes == 1:
        return f"{hours} hours, {minutes} minute"
    elif hours == 1 and minutes > 1:
        return f"{hours} hour, {minutes} minutes"
    elif hours == 1 and minutes < 1:
        return f"{hours} hour, {minutes} minutes"
    elif hours < 1 and minutes == 1:
        return f"{hours} hours, {minutes} minute"
    else:
        return f"{hours} hours, {minutes} minutes"


def main():
    print(time_converter(45))


if __name__ == "__main__":
    main()
