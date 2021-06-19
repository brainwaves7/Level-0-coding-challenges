#Task 0.9 (Vowel outputing function)
print("Task 0.9")

def vowel_in_string (some_string):
    result = []
    vowel =['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    some_string = some_string.casefold()
    
    for element in some_string:
        if element in vowel:
            while element not in result:
                result.append(element)
    
    print(f"Vowels: {result}")

    
vowel_in_string("Umuzi")