from nltk import *
import string

class CleanTesting:
    test_file = open("test.csv", "r")
    test_text = test_file.read()
    test_lines = test_text.split("\n")
    test_lines = [1:] #remove title of testing data