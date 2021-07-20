def vowels_in_string(a_string):
    result = []
    vowels = ["a", "e", "i", "o", "u"]

    a_string = a_string.casefold()

    for element in a_string:
        if element in vowels and element not in result:
            result.append(element)

    result = ", ".join(result)

    print(f"Vowels: {result}")


def main():
    vowels_in_string("Umuzi")


if __name__ == "__main__":
    main()
