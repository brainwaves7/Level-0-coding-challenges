def maximum(*numbers):
    largest_number = numbers[0]
    for element in numbers:
        if element >= largest_number:
            largest_number = element
    return largest_number


print(maximum(9, 15, 3))

# Bonus addition works with orginal function

print(maximum(1, 22, 3, 2))
