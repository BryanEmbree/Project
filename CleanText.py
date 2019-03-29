from nltk import *
import string

class CleanText:
    text = open("train.csv", "r")
    stop_word_file = open("stop_words.lst", "r")
    cleaned_examples = open("cleaned.txt", "w+")
    ps = PorterStemmer()
    stop_words = stop_word_file.read()
    stop_word_file.close()
    stop_word_list = stop_words.split("\n")
    stop_word_set = set(stop_word_list)
    training_data = text.read()
    text.close()
    values = training_data.split("\n") #split at each line, remove the last empty line and the first line header
    values = values[1:-1]
    attributes = []
    
    for attr in values:
        attributes.append(attr.split(","))
    i = 0
    while (i < len(attributes)):
        attributes[i][0] = " " + attributes[i][0] + " "
        attributes[i][0] = attributes[i][0].replace("-", " ")
        attributes[i][0] = attributes[i][0].replace("#", " ")
        attributes[i][0] = attributes[i][0].replace("'", "")
        attributes[i][0] = attributes[i][0].replace(".", " ")
        attributes[i][0] = attributes[i][0].replace("?", " ")
        attributes[i][0] = attributes[i][0].replace("!", " ")
        attributes[i][0] = attributes[i][0].replace("@", " ")
        attributes[i][0] = attributes[i][0].replace("*", " ")
        attributes[i][0] = attributes[i][0].replace("%", " ")
        attributes[i][0] = attributes[i][0].replace("~", " ")
        attributes[i][0] = attributes[i][0].replace("$", "")
        attributes[i][0] = attributes[i][0].replace("(", " ")
        attributes[i][0] = attributes[i][0].replace(")", " ")
        attributes[i][0] = attributes[i][0].replace("[", " ")
        attributes[i][0] = attributes[i][0].replace("]", " ")
        attributes[i][0] = attributes[i][0].replace("{", " ")
        attributes[i][0] = attributes[i][0].replace("}", " ")
        attributes[i][0] = attributes[i][0].replace("\"", " ")
        attributes[i][0] = attributes[i][0].replace(";", " ")
        attributes[i][0] = attributes[i][0].replace("/", " ")
        attributes[i][0] = attributes[i][0].replace("\\", " ")
        attributes[i][0] = attributes[i][0].replace("^", " ")
        attributes[i][0] = attributes[i][0].replace ("+", " ")
        attributes[i][0] = attributes[i][0].replace ("_", " ")
        attributes[i][0] = attributes[i][0].replace("=", " ") 
        attributes[i][0] = attributes[i][0].replace("&", " and ")
        attributes[i][0] = attributes[i][0].replace(" 1 ", " one ")
        attributes[i][0] = attributes[i][0].replace(" 2 ", " two ")
        attributes[i][0] = attributes[i][0].replace(" 3 ", " three ")
        attributes[i][0] = attributes[i][0].replace(" 4 ", " four ")
        attributes[i][0] = attributes[i][0].replace(" 5 ", " five ")
        attributes[i][0] = attributes[i][0].replace(" 6 ", " six ")
        attributes[i][0] = attributes[i][0].replace(" 7 ", " seven ")
        attributes[i][0] = attributes[i][0].replace(" 8 ", " eight ")
        attributes[i][0] = attributes[i][0].replace(" 9 ", " nine ")
        attributes[i][0] = attributes[i][0].replace(" 1st ", " first ")
        attributes[i][0] = attributes[i][0].replace(" 2nd ", " second ")
        attributes[i][0] = attributes[i][0].replace(" 3rd ", " third ")
        attributes[i][0] = attributes[i][0].replace(" 4th ", " fourth ")
        attributes[i][0] = attributes[i][0].replace(" 5th ", " fifth ")
        attributes[i][0] = attributes[i][0].replace(" 100 ", " hundred ")
        attributes[i][0] = attributes[i][0].replace(" 100% ", " hundred ")
        attributes[i][0] = attributes[i][0].replace(" 10 ", " ten ")
        attributes[i][0] = attributes[i][0].replace("0", " ")
        attributes[i][0] = attributes[i][0].replace("1", " ")
        attributes[i][0] = attributes[i][0].replace("2", " ")
        attributes[i][0] = attributes[i][0].replace("3", " ")
        attributes[i][0] = attributes[i][0].replace("4", " ")
        attributes[i][0] = attributes[i][0].replace("5", " ")
        attributes[i][0] = attributes[i][0].replace("6", " ")
        attributes[i][0] = attributes[i][0].replace("7", " ")
        attributes[i][0] = attributes[i][0].replace("8", " ")
        attributes[i][0] = attributes[i][0].replace("9", " ")
        attributes[i][0] = attributes[i][0].replace(":", " ")
        attributes[i][0] = attributes[i][0].lower()
        remove_numbers = attributes[i][0].split(" ")
    
        tokenized_review = []
        tokens = word_tokenize(attributes[i][0])
        for t in tokens:
            if t not in stop_word_set:
                t = ps.stem(t)
                tokenized_review.append(t)

        cleaned_review = " "
        for r in tokenized_review:
            cleaned_review += r + " "
        cleaned_review = cleaned_review.replace(" ", "", 1)
        attributes[i][0] = cleaned_review
        i += 1
        print(i)

    cleaned_file = open("cleaned.txt", "w+")
    cleaned_string = ""
    k = 1
    for example in attributes:
        cleaned_string += example[0] + "," + example[1] + "\n"
        print(k)
        k += 1
    print(cleaned_string)
    cleaned_file.write(cleaned_string)
    
    cleaned_file.close()


    
               
        

    

        
    

    

        
    
    
   

    
    
        


