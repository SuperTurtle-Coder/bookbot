from stats import book_word_count, character_count, dictionary_sort
import sys

def get_book_text(book_path):
    book_contents = ""
    
    with open(book_path) as book:
        book_contents = book.read()
    
    return book_contents

def main():
    book_all = ""
    word_count = 0
    char_dictionary = {}
    sorted_list_dictionary = []
    
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_all = get_book_text(sys.argv[1])
    word_count = book_word_count(book_all) 
    #print(f"{word_count} words found in the document") 
    char_dictionary = character_count(book_all)
    #print(char_dictionary)
    sorted_list_dictionary = dictionary_sort(char_dictionary)
    #print(sorted_list_dictionary)
    
    
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {sys.argv[1]}...')
    print("----------- Word Count ----------")
    print(f'Found {word_count} total words')
    print("--------- Character Count -------")
    
    for dict in sorted_list_dictionary:
        tempchar = dict["char"]
        tempcount = dict["num"]
        print(f'{tempchar}: {tempcount}')
    print("============= END ===============")
    
main()