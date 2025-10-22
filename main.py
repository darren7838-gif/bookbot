import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import count_words

from stats import character_count

from stats import sort_char_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    total_words = count_words(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    
    character_counts = character_count(book_text)
    sorted_chars = sort_char_counts(character_counts)
    print("--------- Character Count -------")
    for item in sorted_chars:
        char = item["char"]
        if char.isalpha():
            print(f"{char}: {item['num']}")
    print("============= END ===============")





if __name__ == "__main__":
	main()


