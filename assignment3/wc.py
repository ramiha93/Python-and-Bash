#!/usr/bin/python
import sys
import os

linecount = 0
wordcount = 0
charcount = 0

for param_x in sys.argv[1:]:
    # Ensures that it's a file
    if os.path.isfile(param_x):
        # Opens the file
        with open(param_x) as f:
            # Loops through each line
            # as it adds +1 to linecount
            for line in f:
                linecount+=1
                line = line.split(" ")
                # Goes through each word in this line
                # as it adds +1 to wordcount
                for word in line:
                    wordcount+=1
                    # Goes through each letter in this word
                    # as it adds +1 to charcount
                    for letter in word:
                        #!!! I don't count space as a character
                        charcount+=1

            print(linecount, wordcount, charcount, param_x)

            # Resetting values
            linecount = 0
            wordcount = 0
            charcount = 0

        f.closed
