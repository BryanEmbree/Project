import numpy as np
import csv
#--------------------
def loadFile(path, dataType):
    with open(path) as inf:
        reader = csv.reader(inf, delimiter=",")
        matrixName = (list(zip(*reader))[dataType])
    return matrixName
#--------------------
def processClass(input):
    matrixName =[]
    for i in range(len(input)):
        temp = input[i][2:]
        matrixName.append(temp)
    return matrixName
#--------------------
input_test_id = loadFile('data/test.csv', 0)
input_test_class = loadFile('data/predictions.csv', 2)
input_test_class = processClass(input_test_class)
f = open("Formated_Predictions.txt", "a")
temp = "ID CLASS"
f.write(temp)
f.write("\n")
for i in range(len(input_test_id)):
    temp = input_test_id[i]+" "+input_test_class[i]
    f.write(temp)
    f.write("\n")
f.close()
#print ("Fin
