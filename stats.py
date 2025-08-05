file_path = "/Users/frankyscomputer/Workspace/github.com/francescogaudio/bookbot/books/frankenstein.txt"

def get_book_text(fp):
    with open(fp,"r", encoding="utf-8") as f:    
        frankenstein = f.read()
    return frankenstein
    
def word_count():
    story_time = get_book_text(file_path)
    words = story_time.split()
    number_of_words = len(words)
    return f"{number_of_words} words found in the document"

def character_count():
    character_count_list = {}
    string_of_words = get_book_text(file_path)
    lower_case = string_of_words.lower()
    for i in lower_case:
        letter = i
        if letter in character_count_list:
            character_count_list[i] += 1
        else: 
            character_count_list[i] = 1
    return character_count_list