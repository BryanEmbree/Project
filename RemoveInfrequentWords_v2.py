import numpy as np
from textblob import classifiers
from textblob import TextBlob
from nltk import *

class RemoveInfrequentWords_v2:

    training_data_file = open("cleaned.txt", "r")
    training_entire_text = training_data_file.read()
    training_data_file.close()
    training_tuples = training_entire_text.split("\n")
    training_tuples.remove('')
    examples = []

    for tt in training_tuples:
        example = tt.split(",")
        examples.append(example[0])
     
    review_dict = {}
    word_set = set()
    i = 0
    
    for review in examples:
        review_tokens = word_tokenize(review)
        word_set = word_set.union(set(review_tokens))
        review_dict[i] = (set(review_tokens))
        print(i)
        i += 1
    print(len(word_set))
    print(len(review_dict))
    
    counter = Counter()
    k = 0
    num_words = 0
    for word in word_set:
        last_seen = -1
        for k in range(0, len(review_dict)):
            if word in review_dict[k]:
                counter[word] += 1
                last_seen = k
            k += 1

        if counter[word] <= 2:
            review_dict[last_seen].remove(word)
            print(word)

            #print(word + " removed: " + str(review_dict[last_seen]))
        k = 0
        print(num_words)
        num_words += 1

    single_occurence_file = open("single.txt", "w+")
    write_string = ""
    n = 0
    for n in range(0, len(review_dict)):
        temp_string = str(review_dict[n])
        temp_string = temp_string.replace('{', '')
        temp_string = temp_string.replace('}', '')
        temp_string = temp_string.replace(',', '')
        temp_string = temp_string.replace('\'', '')
        temp_string += "\n"
        write_string += temp_string
    print(write_string)
    single_occurence_file.write(write_string)
    single_occurence_file.close()

    