from stats import get_num_words, character_count, sort_characters
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path_to_file = sys.argv[1]

def get_book_text():
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text()
    num_words = get_num_words(text)
    character_dict = character_count(text)
    sorted_chars = sort_characters(character_dict)
    # count_characters = character_count(text)
    # print(f"{num_words} words found in the document")
    # print(count_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")


main()