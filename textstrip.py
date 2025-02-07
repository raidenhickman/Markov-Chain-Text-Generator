import os
import string

dashes = "-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-"

'''
This strips files that are in the Data folder down to the bare minimum - only lowercase text and numbers.
'''

print(dashes)

files = os.listdir('.\\data')

for i in files:
	print(i)

print(dashes)

filename = input("Input a file name: ")

with open(".\\data\\" + filename + ".txt", 'r+', encoding="utf8") as openfile:
	text = openfile.read()
	text = " ".join(text.split())
	text = text.translate(str.maketrans('', '', string.punctuation))
	text = text.lower()
	openfile.seek(0)
	openfile.truncate(0)
	openfile.write(text)

	print("Text stripped successfully.")