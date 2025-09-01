def get_book_text(book_path):
    book_contents = ""
    
    with open(book_path) as book:
        book_contents = book.read()
    
    return book_contents

def main():
    from stats import book_word_count
    book_all = ""
    word_count = 0
    
    book_all = get_book_text("books/frankenstein.txt")
    
    word_count = book_word_count(book_all) 
    
    print(f"{word_count} words found in the document")    
    
main()