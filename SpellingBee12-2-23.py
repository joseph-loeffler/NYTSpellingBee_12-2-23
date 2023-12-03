yellow_letter = set(['c'])
letters = set(['g', 'h', 'a', 'i', 'm', 'n', 'c'])

file = open("dictionary.txt")
dict = file.readlines()

answerList = []
for word in dict:
    word = word.strip()
    if len(word) > 3:
        w = set(word)
        if (len(w & yellow_letter) == 1) and (len(w - letters) == 0):
            answerList.append(word)

print(answerList)
print(len(answerList))