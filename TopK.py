
class TopK:
    chi_top_k_attributes = open("ChiTopK.txt", "w+")
    ig_top_k_attributes = open("IGTopK.txt", "w+")
    chi_raw = open("Chi Selection Variables.txt", "r") #requires this file (copy-paste from Weka feature selection)
    ig_raw = open("IG Selection Variables.txt", "r") #requires this file (copy-paste from Weka feature selection)
    chi_text = chi_raw.read()
    ig_text = ig_raw.read()
    chi_raw.close()
    ig_raw.close()


    k = 10 #modify this
    split_chi = chi_text.split("\n")
    split_ig = ig_text.split("\n")
    chi_line = split_chi[-3] #get the third last line
    ig_line = split_ig[-3]
    chi_values = chi_line.split(",")
    ig_values = ig_line.split(",")
    class_number = len(chi_values) + 1
    chi_values = chi_values[0:-1]
    ig_values = ig_values[0:-1]
    chi_first_colon = chi_values[0].find(":")
    ig_first_colon = ig_values[0].find(":")
    chi_values[0] = (chi_values[0])[chi_first_colon + 2:]
    ig_values[0] = (ig_values[0])[ig_first_colon + 2:]
    
    chi_string = ""
    ig_string = ""
    count = 0
    while count < k:
        chi_string += chi_values[count] + ","
        ig_string += ig_values[count] + ","
        count += 1
    
    chi_top_k_attributes.write(chi_string + str(class_number))
    ig_top_k_attributes.write(ig_string + str(class_number))
    chi_top_k_attributes.close()
    ig_top_k_attributes.close()



    
   