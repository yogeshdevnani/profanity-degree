#Version 1.0
#It just checks for words from a hard-coded dictionary.

import os
import nltk

from nltk import tokenize


def processWords():
    # colors are used to describe other things as well
    # hence, if a {skin color} + attribute is what you are looking for - add brown guy
    # so next time any sentence that just uses the color black won't be marked as offensive
    dictList = []

    for line in dictWords.readlines():
        if line == '\n':
            continue
        dictList.append(line.strip())

    for sentence in dataFile:
        offenseCount = 0
        for offensiveWord in dictList:
            if offensiveWord in sentence:
                try:
                    numberSentence =  len(tokenize.sent_tokenize(sentence))
                except:
                    print ("Seems, this is the first time for this program on this machine. \nDownloading a dependency.\t")
                    nltk.download('punkt')
                    numberSentence = len(tokenize.sent_tokenize(sentence))
                offenseCount += 1
                print (sentence,end=" ")
                print ("Profanity Degree: ", degreeCalc(offenseCount, len(sentence.split()),numberSentence))
                print ("")


def addWord():
    wordToAdd = input("Type in the word that I missed: - Type 'exit' to exit \t")
    print (wordToAdd)
    if wordToAdd == 'exit':
        return
    elif (wordToAdd == ""):
        addWord()
    dictAddWords.write(wordToAdd + "\n")



def modifyWords():
    print ("1. Append a new file to existing file.")
    print ("2. Change the existing list of words.")
    temp = input("Enter your input:\n")
    fileNames = os.listdir("dictionary")
    for i in range(len(fileNames)):
        print (i+1,"\t",fileNames[i])
    fileChoice = int(input("Enter the desired file number.\t"))
    tempDir = "dictionary\\" + fileNames[fileChoice - 1]
    newWordList = open(tempDir, 'r')
    if temp == '1':
        dictAddWords.write("\n"+newWordList.read())
        tempInput = input("File Modified Successfully! \n Remove the other file? Y/N\n")
        newWordList.close()
        if tempInput.lower() == 'y':
            os.remove(tempDir)
    elif temp == '2':
        dictWriteWords = open("dictionary/wordsToLook.txt", 'w')
        dictWriteWords.write(newWordList.read())
        dictWriteWords.write("\n")
        newWordList.close()
        os.remove(tempDir)
        dictWriteWords.close()

def changeData():
    fileNames = os.listdir("data")
    for i in range(len(fileNames)):
        print (i+1,"\t",fileNames[i])
    temp = int(input("Enter new file number to replace with existing data:\t"))
    tempDir = "data/" + fileNames[temp-1]
    closeProgram()
    os.replace(tempDir, "data/mainData.txt")


def degreeCalc(offensiveCount, totalCount,numberSentence):
    degree = ((offensiveCount/totalCount) + (offensiveCount/numberSentence)) / 2
    return degree




def closeProgram():
    dataFile.close()
    dictWords.close()
    dictAddWords.close()


def menu():
    while True:
        print ('1. View Results')
        print ('2. Add a new word')
        print ('3. Modify Word List')
        print ('4. Change Data Set')
        print ('5. View ReadMe')
        print ("Enter 'exit' to exit")
        temp = input("Enter your choice:\t")
        if temp == '1':
            processWords()
        elif temp == '2':
            addWord()
        elif temp == '3':
            modifyWords()
        elif temp == '4':
            changeData()
            print ("Updated Successfully. Please open the program again to use.")
            break
        elif temp == '5':
            os.startfile("README.md")
        elif temp.lower() == 'exit':
            closeProgram()
            print ("Closing program.")
            break


dataFile = open("data/mainData.txt",'r')
dictWords = open("dictionary/wordsToLook.txt",'r')
dictAddWords = open('dictionary/wordsToLook.txt', 'a')
menu()
