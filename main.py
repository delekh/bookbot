from stats import get_num_words, get_character_count, get_ordered_character_count
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_num_words(text)   
    char_count = get_character_count(text)
    ordered_char_count = get_ordered_character_count(char_count)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for char in ordered_char_count:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")
main()