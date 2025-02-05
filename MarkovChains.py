import os
import random
import sys

files = os.listdir('.\\data')
text = ""
valid = {}
output_text = ""

print("Please pick from one of the following training data files contained in the data folder. Add your own and run the program again to include alternative data.\n\n" + "\n".join(files))
print("\nNote: The longer the file, the longer it will take; the selected file is read every time the program is started to facilitate inserting your own files.")
filename = input("Type one of the above file names: ")

openfile = open(".\\data\\" + filename, "r", encoding = "utf8")
text = list(openfile.read())
print("Once you begin generating, press enter to generate again. Press any other key and then press enter to quit the program.")
NUMBER = int(input("Input a number equal to or more than 2. Lower = less accurate but faster, higher will cause it to output direct training data: "))


for i in range(NUMBER, len(text)):
    current_letter = text[i]
    recent_letters = ''.join(text[i-NUMBER:i])
    if recent_letters in valid:
        valid[recent_letters].append(current_letter)
    else:
        valid[recent_letters] = [current_letter]

openfile.close()

def generatetext():
    def startercreator():
        return random.choice([key for key in valid.keys() if key[0].isupper() and key[1].islower()])

    output_text = startercreator()

    while True:
        key = output_text[-NUMBER:]
        if key not in valid:
            output_text += startercreator()
            continue

        next_letter = random.choice(valid[key])
        output_text += next_letter
        
        if output_text[-4:] in ["tion", "ness", "ment", "ship"] or output_text[-3:] in ["ity", "ism", "ant", "age", "ery"]:
            break
    print(output_text)

while True:
    generatetext()
    keepgoing = input()
    if keepgoing != "":
        sys.exit()
    
