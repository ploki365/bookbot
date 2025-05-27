from stats import count_words, count_characters, sort_num_char


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    path_to_file = "books/frankenstein.txt"

    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {path_to_file}...")

    print("----------- Word Count ----------")
    num_words = count_words(get_book_text(path_to_file))
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    num_char = sort_num_char(count_characters(get_book_text(path_to_file)))
    for char in num_char:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============")

main()