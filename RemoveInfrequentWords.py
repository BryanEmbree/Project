import numpy as np
from textblob import classifiers
from textblob import TextBlob
from nltk import *

class RemoveInfrequentWords:

    training_data_file = open("cleaned.txt", "r")
    training_entire_text = training_data_file.read()
    training_data_file.close()
    training_tuples = training_entire_text.split("\n")
    training_tuples.remove('')
    examples = training_tuples
    #examples = examples[0:-39000] this is for testing purposes
    review_dict = {} #having this as a dictionary makes no sense but i dont want to go back and chnange the implementation, it works
    word_set = set() #set of all unique words
    i = 0
    
    for review in examples:
        review_tokens = word_tokenize(review)
        word_set = word_set.union(set(review_tokens)) #add to the word_set
        review_dict[i] = (set(review_tokens)) #store each review indexed by i as a set of the words contained in the review
        print(i)
        i += 1
    print(len(word_set))
    print(len(review_dict))
    
    counter = Counter()
    k = 0
    write_string = ""
    num_words = 0
    bad_words = set()
    for word in word_set:
        last_seen = -1 #keeps track of the index of the last review that contains 'word' (there is guarenteed to be at least one)
        print(word)
        for k in range(0, len(review_dict)):
            if word in review_dict[k]:
                counter[word] += 1 #count the number of occurences of that word
                last_seen = k #this is the position of review_dict that contained the last occurence of 'word'
            k += 1 

        if counter[word] == 1: #if 'word' only occured once, revmove it from the review (the set of words in that review)
            review_dict[last_seen].remove(word)
            print(word + " removed: " + str(review_dict[last_seen]))
            bad_words.add(word) #build up the bad word list (removed later, cant remove from word_list directly because it causes an error)

        k = -1 #reset k
        print(num_words) #count the total number of words processed so far
        num_words += 1

    print("found bad words!")
    print(str(bad_words))
    single_occurence_file = open("RemoveInfrequentWords_out.csv", "w+")
    word_set = word_set.difference(bad_words)
    print("remaining")
    print(str(word_set))
    write_string = ""
    num_reviews = 1
    for ex in examples: #for every review of the input file (line by line)
        temp_string = "" #build the review from this
        example_tokens = word_tokenize(ex.replace(',', "")) #tokenize the review (doesn't delete duplicates)
        for token in example_tokens: #for every word in the review, add it to temp_string the number of times it occurs if it's in the word_set
            if token in word_set:
                temp_string += token + " "
        if "positive" in temp_string: #add the proper class back to the end
                temp_string = temp_string.replace("positive", "")
                temp_string += ",positive"
        elif "negative" in temp_string:
                temp_string = temp_string.replace("negative", "")
                temp_string += ",negative"
        else:
                temp_string = temp_string.replace("neutral", "")
                temp_string += ",neutral"
        temp_string += "\n"
        write_string += temp_string #add a newline char and add it to the write_string
        print(temp_string)
        print(num_reviews)
        num_reviews += 1
    
    
    print(write_string)
    single_occurence_file.write(write_string) #print the write_string
    single_occurence_file.close()  
    
    