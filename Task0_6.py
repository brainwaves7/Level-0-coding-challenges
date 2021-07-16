def maximum(*numbers):
    largest_number = numbers[0]
    for element in numbers:
        if element >= largest_number:
            largest_number = element
    return largest_number


if __name__ == "__main__":
    print(maximum(9, 15, 3))
    print(maximum(1, 22, 3, 2))
