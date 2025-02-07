import os
import string

'''
Example file using trainer.py to autocomplete phrases entered by the user.
genwords is how many words in the future to predict.
'''

genwords = 1

# trainer.py start
files = os.listdir('.\\data')
valid = {}
depth = 3

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

while True:
	autocomplete = input("Input text to autocomplete based on the data: ")
	for i in range(0, genwords):
		autocomplete = " ".join(autocomplete.split()[-depth:])
		print(max(set(valid[autocomplete]), key=valid[autocomplete].count))
		autocomplete += " " + max(set(valid[autocomplete]), key=valid[autocomplete].count)