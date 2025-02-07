import os
import random
import sys


genwords = 100 

'''
This is a letter based generator; instead of generating nonsense sentences, it generates nonsense words. This is a slightly edited version of nonsense_generator.py - a trainer for letters + an autocomplete for letters were not included because it gets redundant and bloated, so this is a proof-of-concept more than anything to show the versatility and simplicity of the Markov generator I've made.

See comments in nonsense_generator.py and trainer.py.
'''

files = os.listdir('.\\data')
valid = {}
depth = 2

for file in files:
    with open(".\\data\\" + file, "r", encoding="utf8") as openfile:
        text = list(openfile.read())
        for i in range(depth, len(text)):
            current_word = str(text[i])
            recent_words = " ".join(text[i-depth:i])
            
            if recent_words in valid:
                valid[recent_words].append(current_word)
            else:
                valid[recent_words] = [current_word]


def startgen():
    return random.choice(list(valid.keys()))

def generatetext():
    text = startgen().split()
    
    for i in range(0, genwords):
        key = " ".join(text[-2:])
        if key in valid:
            text.append(random.choice(valid[key]))
        else:
            text.extend(startgen().split())
    
    print("".join(text))

while True:
    dashes = "-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-"
    generatetext()
    keepgoing = input()
    if keepgoing != "":
        sys.exit()