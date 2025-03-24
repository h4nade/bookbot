
import sys
from stats import get_num_words, get_char_count

def main():
    print(sys.argv)
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    get_book_text(book_path)
    # get_book_text('./books/frankenstein.txt');

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        num_words = get_num_words(file_contents)
        print("============ BOOKBOT ============")
        print("Analyzing book found at " + str(filepath) + "...")
        print("----------- Word Count ----------")
        print("Found " + str(num_words) + " total words")
        print("--------- Character Count -------")
        print(get_char_count(file_contents))
        print("============= END ===============")



main();