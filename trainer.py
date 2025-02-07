import os

'''
This is a base for word based Markov chains that I made.
It uses every file in the Data folder to create a dictionary of words which can then be used to generate output text.
Essentially, include more files with more text to be more accurate. Make sure files are sanitised with textstrip.py first!

Alter the depth variable to make the dictionary include more words as the key. This will make the outputs closer to the source text.

On its' own, this does nothing visible.
'''

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