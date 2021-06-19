#Task 0.6
def maximum(a, b, c):
    highest = 0
    if a > b and a > c :
        highest = a
    elif b > a and b > c:
        highest = b
    else:
        highest = c
    return highest

print(maximum(9, 15, 3))

#Bonus addition

def maximum(a, b, c, d):
    highest = 0
    if a > b and a > c :
        highest = a
    elif b > a and b > c:
        highest = b
    else:
        highest = c
    
    if highest < d:
        highest = d
    
    return highest

print(maximum(1, 22, 3, 2))
