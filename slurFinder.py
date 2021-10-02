#  To run program :

#  python slurFinder.py

# Codes explained in comment form

import re
tweets= "This is a good story but can we add more crazy stuff into it. So more users will be clicking on our ads who the hell cares those stupid people , Let's start making new crazy stuff  And also what the hell is wrong with our politics in India ! Those morons are useless and they make stupid rules that we're bound to follow and i hate that crap"

sentence_array = []                                                      # To store array of sentences from paragraph
sentence_array = re.split("[.,;!  ] ", tweets)                           # To split sentences from paragraph based on different special characters

slurs = ['bad', 'hell', 'crazy', 'crap', 'hate', 'stupid', 'useless']    # List of slurs to filter out in sentences


def mainFunction():                                   # Main function  to loop each sentences 
    c= 0
    while c < len(sentence_array):
        slurCount=0

        words_len_in_sentence = len(sentence_array[c].split())                            # Total number of words in sentence
        words_in_sentence = sentence_array[c].split()                                     # Splitting each words from sentences

        slurCalculator(words_in_sentence,words_len_in_sentence, sentence_array[c], c)      # send data to slurCalculator() function 
        c += 1


def slurCalculator(words, length, sentence, count):     # slur calculator function 
    slurCount= 0
    iterate= 0

    while iterate < length:                    # iterate number of words in each sentence
        checkWord= words[iterate]
        iterate += 1

        for x in slurs:                        # after iterating words compare each word slur array 
            if checkWord == x:
                slurCount += 1

    print("Sentence" , count,":", sentence)                # Print each sentence with number
    print("Slur count: " , slurCount)                      # Print number of slur in a sentence
    Percentage = (slurCount * 100) / length                # Calculate slur percentage in each sentence
    print("Slur percentage: " , int(Percentage) ,"%")      # Print slur percentage
    print('')




print("TWEET PARAGRAPH: ")           # Print whole tweet ones
print(tweets)
print('')
print("SEPARATE SENTENCES: " ) 
for sen in sentence_array:
    print(sen)                       # Loop and print all the sentences separated from tweet 

slurLength= len(slurs)               # length of slur array
print('')
print("Slurs:" , slurs)              # Print all slur 
print('')

mainFunction()                       # Run main function 