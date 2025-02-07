import os
import random
import sys

'''
Example file using trainer.py to generate nonsense text based on the source text.
Default data is clean, but when used with punctuation and capitalisation it works just as well and looks more like realistic sentences.
'''

dashes = "-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-"
genwords = 100

# trainer.py start
files = os.listdir('.\\data')
valid = {}
depth = 2

for file in files:
    with open(".\\data\\" + file, "r", encoding="utf8") as openfile:
        text = openfile.read().split()
        for i in range(depth, len(text)):
            current_word = str(text[i])
            recent_words = " ".join(text[i-depth:i])
            
            if recent_words in valid:
                valid[recent_words].append(current_word)
            else:
                valid[recent_words] = [current_word]
# trainer.py end

def startgen():
    return random.choice(list(valid.keys())) # return a random valid key

def generatetext():
    text = startgen().split()
    
    for i in range(0, genwords):
        key = " ".join(text[-2:])
        if key in valid:
            text.append(random.choice(valid[key])) # if the key is valid: add a random word that comes after it to the text
        else:
            text.extend(startgen().split()) # if the key is not valid: add a random valid key to the text
    
    print(" ".join(text)) # print the text in a readable format

while True: # allows generating text repeatedly
    print(dashes)
    generatetext()
    keepgoing = input()
    if keepgoing != "":
        sys.exit()