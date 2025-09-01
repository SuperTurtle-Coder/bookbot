def book_word_count(book_contents):
    word_count = 0
    word_array = []
    
    word_array = book_contents.split()
    
    for word in word_array:
        word_count += 1
    
    return word_count