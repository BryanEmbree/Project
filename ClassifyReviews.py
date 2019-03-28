import numpy as np
from textblob import classifiers
from textblob import TextBlob

class ClassifyReviews:

    training_data_file = open("cleaned_copy.csv", "r")
    training_entire_text = training_data_file.read()
    training_data_file.close()
    training_tuples = training_entire_text.split("\n")
    training_tuples.remove('')
    tuples = []
    i = 1
    for tt in training_tuples:
        review_and_class = tt.split(",")
        new_tuple = (review_and_class[0], review_and_class[1])
        tuples.append(new_tuple)
    classifier = classifiers.NaiveBayesClassifier(tuples)
    print("done")

    
    