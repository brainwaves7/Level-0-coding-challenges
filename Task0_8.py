def time_converter(number):
    hours = round(number / 60)
    minutes = round(number % 60)

    if hours == 1 and minutes == 1:
        return f"{hours} hour, {minutes} minute"
    elif hours > 1 and minutes == 1:
        return f"{hours} hours, {minutes} minute"
    elif hours == 1 and minutes > 1:
        return f"{hours} hour, {minutes} minutes"
    else:
        return f"{hours} hours, {minutes} minutes"


def main():
    print(time_converter(135))


if __name__ == "__main__":
    main()
