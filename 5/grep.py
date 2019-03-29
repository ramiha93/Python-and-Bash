#!/usr/bin/python
import sys
import re

# HOW TO RUN IN TERMINAL:
# python3 grep.py <regex_file> <sourcefile_to_handle> <--highlighter(optional)>

# Saves arguments in corresponding variables
regex_file = sys.argv[1]
sourcefile_to_handle = sys.argv[2]
is_highlighter = sys.argv[3]
# try:
#     print("With highlighter.")
#     is_highlighter = sys.argv[3]
# except:
#     print("No highlighter.")

# Open regexfile and sourcefile
file_syntax = open(regex_file,'r')
file_sourcefile = open(sourcefile_to_handle,'r')

regex_list = list()

# Handles regex
for line in file_syntax:
    print("Test: appending: " + line) ##TESTEST
    regex_list.append(line)

# Reads sourcefile and handles regex occurences
with open(sourcefile_to_handle) as f:
    # Save entire sourcefile in a string
    data = f.read()
    print(data) ##TESTEST

    # Initializing color material
    start_code = "\033[{}m".format(31)
    end_code = "\033[0m"

    for regex_element in regex_list:
        # Adding parenthesis for easier use in "re.sub" later on
        syn_regex_full = '(' + regex_element + ')'

        # if --highligher then give colors to relevant text
        if(is_highlighter == "--highlighter"):
            print("COLORING SELECTED TEXT...") ##TESTEST
            data = re.sub(syn_regex_full, start_code + r'\1' + end_code, data)

        regexp = re.compile(regex_element)
        print(data.splitlines())
        # for line in data:
        #     print(line)
        #     if regexp.search(line):
        #         print(line)
    print(data) ##TESTEST

f.close()

# Closes syntax file and theme file
file_syntax.close()
file_sourcefile.close()
