# Lists and Tuples

'''
Overview: Lists and Tuples are simple ways to store data. Both can hold
any kind of data (strings, numbers, booleans, other lists/tuples, etc).
The main difference between the two is that tuples are IMMUTABLE, meaning
they cannot be changed. For example, a tuple can't be appended to. Instead,
a new tuple would need to be created with the old values plus the new values.
In order to use an array, a separate package is required, so they won't be 
covered in this file as the focus is on Python's built-in features.
'''

# Example of a [list]
list1 = [1, 2, 3, 4, 5, 'word']
print(list1) # Output: [1, 2, 3, 4, 5, 'word']

# Many list methods and functions, like `len()` and `append()`, are available for lists.
# To see a full list of methods for lists, see 'methods.py' in the 'basics' folder
print(len(list1)) # Output: 6

# Example of a (tuple)
tuple1 = (1, 2, 3, 4, 5, 'word', [6, 7, 8])
print(tuple1) # Output: (1, 2, 3, 4, 5, 'word', [6, 7, 8])

# Tuples can be created without using ()
tuple2 = 1, 2, 'characters'
print(tuple2) # Output: (1, 2, 'characters')

# Python starts with 0 for indexing just like any other language
print(list1[5]) # Output: word

# Accessing lists/tuples inside a list/tuple is simple
print(tuple1[6][1]) # Output: 7

# Indexing is also done with negative numbers to go in the opposite direction (starting at -1)
print(list1[-1]) # Output: word

# Slicing in Python is easy `[x:y]` where 'x' is inclusive and y is non-inclusive
print(list1[0:2]) # Output: [1, 2]

# Adding a third value adds the direction (and skip/pattern) of the slice
# Note that the second value is blank because the index '0' would be non-inclusive
print(list1[1::-1]) # Output: [2, 1]
print(list1[0:4:2]) # Output: [1, 3] - the third value of '2' means move forward skipping every other value


# Leaving a value empty defaults the value...
# Example: list1[a:b:c]
# The default value for 'a' is index '0' (inclusive - the start of the list)
# The default value for 'b' is the last index of the list (inclusive - the end of the list)
# The default value for 'c' is '1' (sorts the list forwards starting at index '0' skipping no values)


# Both lists and tuples can be 'unpacked'

# This assigns 'a' to '10' and 'b' to '20'
a, b = [10, 20]
print(a, b) # Output: 10 20

# Similarly, this assigns 'c' to '10 and d' to 'string'
c, d = (10, 'string') # Equivalent to: c, d = 10, 'string'
print(c, d) # Output: 10 string

# Strings can be split into lists and tuples
string1 = 'This is a test'
print(string1.split()) # Output: ['This', 'is', 'a', 'test']

# Adding a character/symbol in the parenthesis splits the string on that value
print(string1.split('t')) # Output: ['This is a ', 'es', ''] - characters are case sensitive

# The `list()` built-in function attempts to create a list out of the argument (separates strings by each character)
print(list(string1)) # Output: ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 't', 'e', 's', 't']

# The `tuple()` built-in function attempts to create a tuple out of the argument (works the same way `list()` works)
print(tuple(string1)) # Output: ('T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 't', 'e', 's', 't')

# The `join()` built-in function combines the list/tuple into a string
print('GAP'.join(['one', 'two', 'three', 'four'])) # Output: oneGAPtwoGAPthreeGAPfour
print('GAP'.join(('one', 'two', 'three', 'four'))) # Output: oneGAPtwoGAPthreeGAPfour
# Notice the string 'GAP' acts as the value between each element of the list/tuple

# The `str()` built-in function turns a value into a string (this example uses a tuple)
tuple_to_string = 1, 2, 'word'
print(str(tuple_to_string)) # Output: (1, 2, 'word') - it looks like a tuple but it's actually a string

# Other notes
# -----------
# 1. More on built-in functions can be found in 'built_in_functions.py' in the 'basics' folder
