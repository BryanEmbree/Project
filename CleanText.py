from nltk import *
import string

class CleanText:
    text = open("train.csv", "r")
    stop_word_file = open("stop_words.lst", "r")
    cleaned_file = open("CleanText_out.csv", "w+")
    ps = PorterStemmer()
    stop_words = stop_word_file.read()
    stop_word_file.close()
    stop_word_list = stop_words.split("\n")
    stop_word_set = set(stop_word_list)
    stop_word_set.remove('')
    training_data = text.read()
    text.close()
    values = training_data.split("\n") #split at each line, remove the last empty line and the first line header
    values = values[1:-1]
    attributes = []
    cleaned_token_list = []
    
    for attr in values:
        attributes.append(attr.split(","))
    
    #attributes = attributes[0: -39990]
    
    
    i = 0
    while (i < len(attributes)):
        attributes[i][0] = " " + attributes[i][0] + " " #padding so every word has a space at the begining and end
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
        attributes[i][0] = attributes[i][0].replace("|", " ")
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
        attributes[i][0] = attributes[i][0].replace(":", " ") #remove all symbols
        attributes[i][0] = attributes[i][0].lower()

        cleaned_tokens = [] #here we will remove consecutive letters, stop words, and then stop them
        tokens = word_tokenize(attributes[i][0]) #get each word as its own string in a list
        for t in tokens:
            consecutive_removed = "" #used to build up the string and only print non duplicate characters
            if (len(t)) > 2: #othwerise, the token had more than 2 characters and we can remove consecutive letters, if length <= 2, it wont be added
                #print("more than letter token: " + t)  
                consecutive_removed += t[0] #let this string start with the first letter
                for letter in range(1, len(t)): #start from the second letter and look at the one previous as we loop (len(t) > 2)
                    if t[letter] != consecutive_removed[-1]: #if were looking at a letter that has not been just added, add it to the string
                        consecutive_removed += t[letter]
                        #print("nonduplicate " + t[letter] + " seen, add it!")
    
                if consecutive_removed not in stop_word_set: #if out cleaned string isnt a stop word, add it to the list of all reviews, otherwise we dont add it
                    cleaned_tokens.append(consecutive_removed) #add t to the new and cleaned tokens  
                stemmed_tokens = [] #new list to stop stemmed tokens
                for ct in cleaned_tokens: #now stem each word
                    stemmed_tokens.append(ps.stem(ct))  

        cleaned_token_list.append(stemmed_tokens) #add all the strings that made it through to tilter (they are lists) to a list containing all reviews (one review processed now)
        i += 1
        print(i)

    #finally we have our cleaned reviews in cleaned_token_list!
    write_string = ""
    class_index = 0
    for review in cleaned_token_list:
        review_list_strings = []
        temp_string = ""
        for word in review:
            temp_string += word + " "
        temp_string = temp_string[0:-1] #remove last extra space
        temp_string += "," + attributes[class_index][1] + "\n"
        print(temp_string)
        write_string += temp_string #add the review with its cleaned text and its class added back
        class_index += 1
        
    write_string = write_string[0:-1]
    cleaned_file.write(write_string) #print to the file CleanText_out.csv
    cleaned_file.close()




    
               
        

    

        
    

    

        
    
    
   

    
    
        


