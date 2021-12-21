#Version 1.0
#It just checks for words from a hard-coded dictionary.




def main():
    ## + function skinColor + man
    # colors are used to describe other things as well
    # hence, if a {skin color} + attribute is what you are looking for
    # for example {black man} - simply add 'black+man' to the dictionary - becomes {black man} with below code
    # so next time any sentence that just uses the color black won't be marked as offensive

    for index in range(len(dictList)):
        if "+" in dictList[index]:
            dictList[index] = dictList[index].replace("+", " ")

    for sentence in dataFile:
        offenseCount = 0
        for offensiveWord in dictList:
            if offensiveWord in sentence:
                offenseCount += 1
                print (f'{"found", offensiveWord, sentence}')
        print (f'{"Profanity Degree ", degreeCalc(offenseCount, len(sentence.split()))}')



def addWord():
    wordToAdd = input("Type in the word that I missed: - Type 'exit' to exit \t")
    if wordToAdd == 'exit':
        return
    elif (wordToAdd == ""):
        addWord()
    dictAddWords.write(wordToAdd+"\n")
    addWord()


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
    print ('3. Change Word List')
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
        print("")
    elif temp == '4':
        print("")
    elif temp == '5':
        print()
    elif temp == '0':
        print()
    elif temp.lower() == 'e':
        closeProgram()

dataFile = open("data/content.txt",'r')
dictWords = open("dictionary/wordsLevel1.txt",'r')
dictList = dictWords.read().split()
dictAddWords = open('dictionary/wordsLevel1.txt', 'a')
main()
