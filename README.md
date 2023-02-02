A program to indicate the degree of profanity in text.

This script gets the data(twitter's data) from data folder. The mainData.txt has all the data that will be parsed. You can put other text files in the folder and update those by running the program in a Python editor.
Dictionary contains 'wordsToLook.txt', that contains the word that will be flagged. You may add other text files and append/ replace the existing words by running the program.

The degree of profanity is calculated by : {[(noOfOffensiveWords)/ (totalNumberOfWords)] + [(noOfOffensiveWords)/ (totalNumberOfSentences)]} / 2 - It gives a better degree of profanity, as it includes the number of sentences
Number of sentences are calculated using nlkt (dependency included).

This script has been made for a personal project.
It is being kept public.
