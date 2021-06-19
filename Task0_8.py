#Task 0.8 (Number to time converting function)
print("Task 0.8")

def time_converter(number):
    hours = 0
    minutes = 0
    
    while number >= 60: 
        hours += 1
        number -= 60
    
    if number < 60:
        minutes = number
    
    if hours == 1 and minutes == 1:
        print(f"{hours} hour, {minutes} minute")
    elif hours > 1 and minutes == 1:
        print(f"{hours} hours, {minutes} minute")
    elif hours == 1 and minutes > 1:
        print(f"{hours} hour, {minutes} minutes")
    elif hours > 1 and minutes > 1:
        print(f"{hours} hours, {minutes} minutes")
    elif hours == 0 and minutes == 1:
        print(f"{minutes} minute")
    elif hours == 0 and minutes > 1:
        print(f"{minutes} minutes")
    elif hours == 1 and minutes == 0:
        print(f"{hours} hour")
    elif hours > 1 and minutes == 0:
        print(f"{hours} hours")
    else:
        print("No number to convert")


    
time_converter(71)  
time_converter(133)