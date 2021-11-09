import re

def hapax(textfiles):
    file = open("textFile.txt","r")
    a = file.read()
    textfiles = a.lower()
    wordCount={}
    for word in file.read().split():
        if word not in wordCount:
            wordCount[hapax]=1
        else:
            wordCount[hapax] +=1
            for hapex in wordCount.items():
                print("The hapax found in the text are:")
                for hapex in textfiles:
                    print(hapex)













