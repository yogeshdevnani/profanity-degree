#Version 1.0
#It just checks for words from a hard-coded dictionary.

import os



def main():
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
                offenseCount += 1
                print (f'{"found", offensiveWord, sentence}')
        # print (f'{"Profanity Degree ", degreeCalc(offenseCount, len(sentence.split()))}')



def addWord():
    wordToAdd = input("Type in the word that I missed: - Type 'exit' to exit \t")
    if wordToAdd == 'exit':
        return
    elif (wordToAdd == ""):
        addWord()
    dictAddWords.write(wordToAdd+"\n")
    addWord()


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
        dictWriteWords = open("dictionary/wordsLevel1.txt", 'w')
        dictWriteWords.write(newWordList.read())
        newWordList.close()
        os.remove(tempDir)
        dictWriteWords.close()



def degreeCalc(offensiveCount, totalCount):
    degree = offensiveCount/totalCount
    return degree




def closeProgram():
    dataFile.close()
    dictWords.close()
    dictAddWords.close()


def menu():
    print ('1. View Results')
    print ('2. Add a new word')
    print ('3. Modify Word List')
    print ('4. Change Data Set')
    print ('5. View ReadMe')
    print ('0. Search Using GOD Mode')
    print ("Enter 'e' to exit")
    temp = input("Enter your choice:\t")
    if temp == '1':
        main()
    elif temp == '2':
        addWord()
    elif temp == '3':
        #modify WordList
        modifyWords()
    elif temp == '4':
        print('')
    elif temp == '5':
        print()
    elif temp == '0':
        print()
    elif temp.lower() == 'e':
        closeProgram()

dataFile = open("data/content.txt",'r')
dictWords = open("dictionary/wordsLevel1.txt",'r')
dictAddWords = open('dictionary/wordsLevel1.txt', 'a')
menu()
