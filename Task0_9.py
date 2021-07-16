def vowels_in_string(a_string):
    result = []
    vowels = ["a", "e", "i", "o", "u"]

    a_string = a_string.casefold()

    for element in a_string:
        if element in vowels:
            while element not in result:
                result.append(element)

    result = ", ".join(result)

    print(f"Vowels: {result}")
