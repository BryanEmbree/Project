#usage python3 sparceARFFGen.py > sparceARFFGen_out.arff
#requires file "RemoveInfrequentWords_out.csv"
import csv

filename = "RemoveInfrequentWords_out.csv"
myset = set()

csvfile = open(filename, newline='')
datareader = csv.reader(csvfile, delimiter=',', quotechar='"')
for row in datareader:
    for word in row[0].split(' '):
        myset.add(word)
csvfile.close()

features = sorted(myset)
#print(features)

print("@RELATION reviews")
for i in range(0, len(features)):
    print(f"@ATTRIBUTE 'a{i}: {features[i]}' NUMERIC")
print("@ATTRIBUTE class {positive,neutral,negative}")
print("@DATA")

csvfile = open(filename, newline='')
datareader = csv.reader(csvfile, delimiter=',', quotechar='"')
for row in datareader:
    fcount = {}
    for word in row[0].split(' '):
        fcount[word] = fcount.get(word, 0) + 1
        #print(f'{word}: {fcount[word]}')

    print('{', end='')
    for i in range(0, len(features)):
        count = fcount.get(features[i], 0)
        if count > 0:
            print(f'{i} {count},', end='')
    print(f'{len(features)} {row[1]}}}')