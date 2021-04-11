import random

with open('words.txt') as wordfile:
    words = wordfile.readlines()

with open('learnedwords.txt', 'a+') as learnedfile:
    learnedwords = learnedfile.readlines()

    new_words = [word for word in words if word not in learnedwords]
    new_word = random.choice(new_words)

    learnedfile.write(new_word)

print(new_word)

