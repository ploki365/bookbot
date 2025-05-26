def count_words(text):
    return len(text.split())

def count_characters(text):
    char_count = {}

    for char in text.lower():
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    
    return char_count