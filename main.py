from stats import *
import sys

def check():
    arguments = sys.argv
    if not len(arguments) == 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    return arguments[1] 

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
    return file_content

def main():
    rel_path = check()
    content = get_book_text(rel_path)
    num_words = count_words(content)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {rel_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_of_char = count_characters(content)
    sorted_chars = sort_characters(num_of_char)
    for unit in sorted_chars:
        print(f"{unit["name"]}: {unit["num"]}")
    print("============= END ===============")
main()
