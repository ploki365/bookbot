def count_words(text):
    return len(text.split())

def count_characters(text):
    char_count = {}

    for char in text.lower():
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    
    return char_count

def sort_num_char(char_count):
    return sorted([{"char": char, "num": num} for char, num in char_count.items()], key=lambda x:x["num"], reverse=True)