file_path = "/Users/frankyscomputer/Workspace/github.com/francescogaudio/bookbot/books/frankenstein.txt"

def get_book_text(fp):
    with open(fp,"r", encoding="utf-8") as f:    
        frankenstein = f.read()
    return frankenstein
    

def main():
    story_time = get_book_text(file_path)
    words = story_time.split()
    number_of_words = len(words)
    print(f"{number_of_words} words found in the document") 

main()