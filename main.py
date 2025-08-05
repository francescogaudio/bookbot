import sys
from stats import word_count, character_count, sorted_letters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]

    print("============ BOOKBOT ============")
    
    print(f"Analyzing book found at {file_path}...")
    
    print("----------- Word Count ----------")
    
    words_in_doc = word_count(file_path)
    print (f"Found {words_in_doc} total words")
    
    characters = character_count(file_path)
    print("--------- Character Count -------")
    
    key_letters = sorted_letters(file_path)
    for entry in key_letters:
        letters = entry["letter"]
        value = entry["count"]
        if letters.isalpha():
            print(f"{letters}: {value}")

main()