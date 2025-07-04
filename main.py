from stats import word_count, char_count, sort_char_count, sort_on
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found 75767 total words")
    print("----------- Character Count -------")
    for item in sorted:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")


def main():
    try:
        path_to_file = sys.argv[1]
        print(path_to_file)
        text = get_book_text(path_to_file)
        word_count(text)
        to_sort = sort_char_count(char_count(text))
        to_sort.sort(key=sort_on, reverse=True)
        print_report(to_sort)
    except:
        print("Usage: python main.py <file name> <path to file>")
        print('Example: python main.py "books/frankenstein.txt"')
        sys.exit(1)


if __name__ == "__main__":
    main()
