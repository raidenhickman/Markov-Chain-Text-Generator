Markov Chain Text Generators

!!!
To work correctly, the program must be in the same folder as a folder named "Data", containing only text documents. Sample data folder included.
!!!


Included In This Project
- A text stripper. Strips text of all punctuation, indentation, and newline characters. Makes all text lowercase.
  Not essential to the function of the project, but useful for making outputs look generally nicer.
  
- A trainer module. Takes all the files in the Data folder and outputs a dictionary called "Valid", based on Markov chains.
  
- 3 example projects using this trainer module - two nonsense generators (one which generates sentences and one which generates words) and one text autocompleter.
  
- A preloaded Data folder with 4 books, all pre-stripped for convenience.
  Includes:
  1984 by George Orwell, from Project Gutenberg
  Dracula by Bram Stoker, from Project Gutenberg
  Moby Dick by Herman Melville, from Project Gutenberg
  The Bible from https://github.com/gratis-bible/bible
