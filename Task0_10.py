#Task 0.10
def common_letters(first_word, second_word):
    result = []
    
    for element in second_word:
        if element in first_word:
            result.append(element)
            
    return (f"Common letters: {result}")
        
print(common_letters("house", "computers"))