

# import manifesto.txt into a string

with open('manifesto.txt') as f:
    # PUT WORDS INTO A LIST OF STRINGS
    word_list=[word for line in f for word in line.split()]
    # REMOVE DUPLICATES FROM LIST
    word_list = list(dict.fromkeys(word_list))
    # PRINT LIST
    # print(word_list)





# separate words by syllable

## loop this function for the length of the word_list


def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if (word[0] in vowels):
        count += 1
    for index in range(1, len(word)):
        if ((word[index] in vowels) and (word[index - 1] not in vowels)):
            count += 1
            if (word.endswith("e")):
                count -= 1
    if (count == 0):
        count += 1
    return count

for word in word_list:
    countedwords = str(syllable_count(word)) + " " + word
    
    words = countedwords.split()
    

    print(words)
    
    

# create array of words for each syllable count
