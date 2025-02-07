import os
import string

files = os.listdir('.\\data')
print(files)
filename = input("Input a file name: ")

with open(".\\data\\" + filename + ".txt", 'r+', encoding="utf8") as openfile:
    text = openfile.read()
    text = " ".join(text.split())
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    openfile.seek(0)
    openfile.truncate(0)
    openfile.write(text)