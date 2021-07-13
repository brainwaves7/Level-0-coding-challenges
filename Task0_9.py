def vowels_in_string(some_string):
    result = []
    vowels = ["a", "e", "i", "o", "u"]

    some_string = some_string.casefold()

    for element in some_string:
        if element in vowels:
            while element not in result:
                result.append(element)

    result = ", ".join(result)

    print(f"Vowels: {result}")


vowels_in_string("Umuzi")
