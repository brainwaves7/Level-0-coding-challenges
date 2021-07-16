def common_letters(first_word, second_word):
    result = []

    for element in second_word:
        if element in first_word:
            result.append(element)

    result = ", ".join(result)

    return f"Common letters: {result}"
