# Strings

'''
Strings are very basic and basically the same as any other language.
Strings can be created with single quotes or double quotes.

Values can be added into strings in various way (Format method or via an f-string).
'''

# Both examples below will result in the same
string1 = 'Test 1'
string2 = "Test 1"
print(string1, string2) # Output: Test 1 Test 1

'''
Quotes can be added inside strings by using single quotes or double quotes on the outside,
then using the opposite on the inside.
'''

string3 = 'The man said "hello world"'
print(string3) # Output: The man said "hello world"

string4 = "The man said 'hello world'"
print(string4) # Output: The man said 'hello world'

# Strings have the usual features such as escaping characters with the forward slash symbol
string4 = 'To use a single quote in this string, use \'this\'!'
print(string4) # Output: To use a single quote in this string, use 'this'!

# \n will create a new line just like any other language
# '''[text]''' can be used like `` from any other language

# Concatenation can be dones with the '+' operator
string5 = 'hello' + ' ' + 'world'
print(string5) # Output: hello world

# Strings can be multiplied via the '*' operator
string6 = 'copypaste ' * 5
print(string6) # Output: copypaste copypaste copypaste copypaste copypaste

# Variables/values can be inserted into string via f-strings (formatted strings)
string7 = 'This person, {}, is {} years old'.format('Bob', 20)
print(string7) # Output: This person, Bob, is 20 years old

# Naming the slots can be done by adding the name into the braces
age = 30
string7 = 'This person, {one}, is {two} years old'.format(one = 'Bill', two = age)
print(string7) # Output: This person, Bill, is 30 years old

# Or, even easier, add an 'f' right before the string to use variables directly in the braces
name = 'John'
age2 = 54

# Operations can also be performed inside the braces
string8 = f'This person, {name}, is {age2 - 10} years old'
print(string8) # Output: This person, John, is 44 years old
