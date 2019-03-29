#!/usr/bin/python
import sys
import re

# HOW TO RUN IN TERMINAL:
# python3 highlighter.py <syntaxfile> <themefile> <sourcefile_to_color>

# Saves arguments in corresponding variables
syntaxfile = sys.argv[1]
themefile = sys.argv[2]
sourcefile_to_color = sys.argv[3]

# Open syntax file and theme files
file_syntax = open(syntaxfile,'r')
file_theme = open(themefile,'r')

name_SynTheme = dict()

# Handles regex and its name
for line in file_syntax:
    syn_regex, syn_name = line.rsplit(':', 1)
    if syn_regex.startswith('"') and syn_regex.endswith('"'):
        #removes quotation marks
        #we assume they all have one of them at the beginning and end
        syn_regex = syn_regex[1:-1]

    syn_name = syn_name.strip() #removes whitespaces
    #save in dictionary
    name_SynTheme[syn_name] = [syn_regex]

# Handles color and its name
for line in file_theme:
    theme_name, color_sequence = line.split(':')
    color_sequence = color_sequence.strip() #removes whitespaces
    #save in dictionary
    name_SynTheme[theme_name].append(color_sequence)

# Reads file to color and handles regex occurences
with open(sourcefile_to_color) as f:

    # Saving entire file in a string
    data = f.read()

    for key in name_SynTheme:
        start_code = "\033[{}m".format(name_SynTheme[key][1])
        end_code = "\033[0m"

        syn_regex_full = '(' + name_SynTheme[key][0] + ')'
        # Turning all comment to specified-colored text
        if(key == "comment2"):
            data = re.sub(syn_regex_full, start_code + r'\1' + end_code, data, flags=re.DOTALL)
        else:
            data = re.sub(syn_regex_full, start_code + r'\1' + end_code, data)

    print(data)
f.close()

# Closes syntax file and theme file
file_syntax.close()
file_theme.close()
