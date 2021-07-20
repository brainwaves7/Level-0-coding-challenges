def common_letters(first_word, second_word):
    result = []

    for element in second_word:
        if element in first_word:
            result.append(element)

    result = ", ".join(result)

    print(f"Common letters: {result}")


def main():
    common_letters("house", "computers")


if __name__ == "__main__":
    main()
