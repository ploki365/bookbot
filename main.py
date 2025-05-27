from stats import count_words, count_characters, sort_num_char
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]

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