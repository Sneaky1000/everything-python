# Order of code execution

'''
- Python ignores whitespace (outside of strings) and empty lines when executing code
- Indendation is extremely important in Python and it even replaces braces when compared to other languages
- Instead of using braces for functions, indentation is used instead (see the 'functions' folder for more details)
- To create "multiple lines" of code in a single line, a semi-colon or '\' can be used to end a line (example below)
'''

# Examples of "multiple lines" of code in a single line
a = 1; b = 2 # Semi-colon

c = 1 + 2 + 3 + \
    7 + 8 + 9 # This line (14) is still read as line 13 upon execution (so adding a comment, for example, after the '\' will break the code

print(c) # Output: 30
