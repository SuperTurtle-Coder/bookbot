#python include file containing statistic based functions for the book bot

#this function counts each word in a book and returns the total word count
def book_word_count(book_contents):
    word_count = 0
    word_array = []
    
    word_array = book_contents.split() #splitting the contents of the book into list of words
                                       #this includes the ".,'" and other odd characters
    
    for words in word_array: #gets total word count of all words in book
        #print(words) //used for debugging
        word_count += 1
    
    return word_count #total word count for book


#this function creates a dictionary for each character (lowercase only)
#returns the dictionary of characters with atribute data of character count
def character_count(book_contents): 
    word_array = []
    char_dictionary = {}
    
    for words in book_contents:#make list of characters to the sort into dictionary
        word_array.append(words.lower())
        #print(words.lower()) #used for debugging
    #print(word_array)    #used for debugging
    
    for char in word_array:#iterate through each character
        dup_key = False #duplicate flag
        #print(char) #used for debugging
        for key in char_dictionary:#iterate through the string keys
            if(char == key):#if the current char in the character list is found in the dictionary keys
                temp = char_dictionary[key] + 1 #update the character count data of that key +1
                char_dictionary[key] = temp
                dup_key = True#update flag for key found
        
        if(dup_key == False):#char was not found in dictionary make new key->value entry and sent value to 1
            char_dictionary[char] = 1    
    
    #print(char_dictionary) #for debugging
    return char_dictionary#return the dictionary
    
    