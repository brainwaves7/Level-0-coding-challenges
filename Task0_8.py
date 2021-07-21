def time_converter(number):
    hours = int(number / 60)
    minutes = int(number % 60)
    hours_text = ""
    minutes_text = ""

    if hours != 1:
        hours_text = "hours"
    else:
        hours_text = "hour"
    if minutes != 1:
        minutes_text = "minutes"
    else:
        minutes_text = "minute"

    return f"{hours} {hours_text}, {minutes} {minutes_text}"


def main():
    print(time_converter(45))


if __name__ == "__main__":
    main()
