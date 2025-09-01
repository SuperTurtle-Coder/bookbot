def get_book_text(book_path):
    book_contents = ""
    
    with open(book_path) as book:
        book_contents = book.read()
    
    return book_contents

def main():
    from stats import book_word_count, character_count, dictionary_sort
    book_all = ""
    word_count = 0
    char_dictionary = {}
    sorted_list_dictionary = []
    book_path = "books/frankenstein.txt"
    
    book_all = get_book_text(book_path)
    word_count = book_word_count(book_all) 
    #print(f"{word_count} words found in the document") 
    char_dictionary = character_count(book_all)
    #print(char_dictionary)
    sorted_list_dictionary = dictionary_sort(char_dictionary)
    #print(sorted_list_dictionary)
    
    
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {book_path}...')
    print("----------- Word Count ----------")
    print(f'Found {word_count} total words')
    print("--------- Character Count -------")
    
    for dict in sorted_list_dictionary:
        tempchar = dict["char"]
        tempcount = dict["num"]
        print(f'{tempchar}: {tempcount}')
    print("============= END ===============")
    
main()