# 5.1
### >> python3 highlighter.py naython.syntax naython.theme hello.ny

I've made my code such that the syntax file and theme file handle their same corresponding line at the same order.

# 5.2
### >> python3 highlighter.py python.syntax python2.theme demo.py
The code in "demo.py" is not made with the purpose of making sense or  correctly compile. It is just to verify that our regexes from "python.syntax" manage to catch what we intend them to catch when we use "demo.py" as our "sourcefile to color" and print it with colors.

Despite example 5.0 showing "def", "for" and "if" with the same color, I have chosen to give each of them different colors so it becomes easier to spot if my regexes are catching the intended text portion of our "sourcefile to color" file.

I assume that:
- a comment is only a one line comment
- there won't be any quotation mark (") inside a string.
- demo.py has a balanced amount of quotation marks and there is no stray quotation mark in our code (in order for our "special statements regex to properly work)

# 5.3
### >> python3 highlighter.py java.syntax java.theme demo.java

The file "demo.java" doesn't necessarily compile as a java code. Its purpose is similar as in 5.2 .

# 5.4
### >> python3 grep.py grep_regex.syntax demo_grep.txt (optional: --highlighter)

We assume that a random argument is given by the user instead of "--highlighter" even if they do not wish to color the selected text.

We assume that the given regexes do not contain quotation marks at their start and end, they are separated by a new line within the syntax file.

(Incomplete, had issues printing out specific lines)
