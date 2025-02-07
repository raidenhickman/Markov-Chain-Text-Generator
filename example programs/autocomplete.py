import os

'''
Example file using trainer.py to autocomplete phrases entered by the user.
genwords is how many words in the future to predict.
'''

dashes = "-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-"
genwords = 1

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

while True: # repeat until theres an error or it's shut off
    print(dashes)
    autocomplete = input("Input text to autocomplete based on the data: ") 
    loops = 0
    for i in range(0, genwords):
        autocomplete = " ".join(autocomplete.split()[-depth:]) # the "autocomplete" variable is set to the last words of itself, matching the depth.
        if autocomplete not in valid.keys() and loops == 0:
            print("No words could not be found in the training data. Consider adding more data.")
            break
        elif autocomplete not in valid.keys() and loops != 0:
            print("No more words could be found in the training data. Consider adding more data.")
            break
        else:
            print(max(set(valid[autocomplete]), key=valid[autocomplete].count)) # the "autocomplete" variable is treated as a key in the valid words dictionary. This returns the most common word that follows that set of words and then prints it.
            autocomplete += " " + max(set(valid[autocomplete]), key=valid[autocomplete].count) # appends the word that was just printed to the autocomplete variable so that it can recursively run.
        loops += 1