def maximum(*numbers):
    largest_number = numbers[0]
    for element in numbers:
        if element >= largest_number:
            largest_number = element
    print(largest_number)


def main():
    maximum(1, 22, 3, 2)


if __name__ == "__main__":
    main()
