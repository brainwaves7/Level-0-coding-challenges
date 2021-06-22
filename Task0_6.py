#Task 0.6
def maximum(*a):
    large = a[0]
    for element in a:
        if element >= large:
            large = element
    return large

print(maximum(9, 15, 3))

#Bonus addition works with orginal function
print(maximum(1, 22, 3, 2))
