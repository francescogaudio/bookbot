#file_path = "/Users/frankyscomputer/Workspace/github.com/francescogaudio/bookbot/books/frankenstein.txt"

def get_book_text(fp):
    with open(fp,"r", encoding="utf-8") as f:    
        book = f.read()
    return book
    
def word_count(file_path):
    story_time = get_book_text(file_path)
    words = story_time.split()
    number_of_words = len(words)
    return number_of_words

def character_count(file_path):
    character_count_list = {}
    string_of_words = get_book_text(file_path)
    lower_case = string_of_words.lower()
    for i in lower_case:
        letter = i
        if letter in character_count_list:
            character_count_list[i] += 1
        else: 
            character_count_list[i] = 1
    dictionary_list = [{"letter": l, "count": c} for l, c in character_count_list.items()]
    return dictionary_list

def sorted_letters(file_path):
    character_count_list = character_count(file_path)
    character_count_list.sort(key=lambda x: x["count"], reverse=True)
    return character_count_list