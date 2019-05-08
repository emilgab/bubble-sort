# imports regular expressions for processing data strings
import re
# imports sys module for accepting command-line arguments
import sys

def data_process(in_file):
    '''
    Returns a list of words found in the file as lowercase and without punctuation.
    '''
    # A list we store our words in
    our_words = []
    
    # Opens the file, splits by word and uses regular expressions on each word. 
    file_opened = open(in_file, mode="r")
    for word in file_opened.read().split():
        # reassigns 'word' to be lowercase and exclude punctuation
        word = re.sub("\W", "", word).lower()
        our_words.append(word)
    
    return our_words
        
def bubble_sort(my_list):
    '''
    Takes a list as input and return this list as sorted by length using bubble sort.
    If words have equal length, then we sort them lexicographically.
    '''
    for number in range(len(my_list)-1,0,-1):
        for item in range(number):
            # Swaps the words if the length of the current word is bigger than the next word
            # This will sort it by increasing length
            if len(my_list[item]) > len(my_list[item+1]):
                my_list[item],my_list[item+1] = my_list[item+1],my_list[item]
                
            # In Python, the string "B" is of greater value than the string "A"
            # We can therefore compare them in order to sort them lexicographically.
            # If the current word is of equal length than the next word,
            # and the word value is greater than the next, we swap them.
            elif len(my_list[item]) == len(my_list[item+1]) and my_list[item] > my_list[item+1]:
                my_list[item],my_list[item+1] = my_list[item+1],my_list[item]
                
    return my_list
                
if __name__ == "__main__":
    try:
        # Allows for command-line arguments,
        if len(sys.argv) == 2:
            file = sys.argv[1]
            for word in bubble_sort(data_process(file)):
                print(word)
        # will ask for filename if no arguments given.
        else:
            file = input("What is the name of the file? ")
            for word in bubble_sort(data_process(file)):
                print(word)
    except:
        print("File not found")