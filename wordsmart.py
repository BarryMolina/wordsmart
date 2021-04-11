import random
import sys

with open('words.txt') as wordfile:
    words = wordfile.readlines()

with open('learnedwords.txt') as learnedfile:
    learnedwords = learnedfile.readlines()

new_words = [word for word in words if word not in learnedwords]
new_word = random.choice(new_words)

#learnedfile.write(new_word)

sys.stdout.write(new_word.capitalize())

