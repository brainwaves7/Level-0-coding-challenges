def maximum(*numbers):
    largest_number = numbers[0]
    for element in numbers:
        if element >= largest_number:
            largest_number = element
    return largest_number
