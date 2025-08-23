from stats import word_count, letter_count, sort_letter_count
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookPath = sys.argv[1]
    text = get_book_text(bookPath)
    word_total = word_count(text)
    letter_total = letter_count(text)
    letter_total_sorted = sort_letter_count(letter_total)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookPath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_total} total words")
    print("--------- Character Count -------")
    for entry in letter_total_sorted:
        if entry ["char"].isalpha():
            print(f'{entry["char"]}: {entry["num"]}')

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
