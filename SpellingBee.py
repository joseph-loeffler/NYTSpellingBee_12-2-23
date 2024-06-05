yellow_letter = set(['c'])
letters = set(['h', 't', 'e', 'c', 'm', 'a', 'n'])

file = open("dictionary.txt")
dict = file.readlines()

answerList = []
anagramList = []
for word in dict:
    word = word.strip()
    if len(word) > 3:
        w = set(word)
        if (len(w & yellow_letter) == 1) and (len(w - letters) == 0):
            answerList.append(word)
            if w == letters:
                anagramList.append(word)

print(answerList)
print(anagramList)