# Dictionaries

# Dictionaries in Python aren't much different from any other programming language

# Dictionaries in Python hold key-value pairs (data type of each key/value doesn't matter)
dict1 = {
  'A': 100,
  'B': 'string',
   1 : [1, 2, 3],
}
print(dict1) # Output: {'A': 100, 'B': 'string', 1: [1, 2, 3]}

# Keys must be unique or they will be overwritten as the dictionary is read
dict2 = {
  'A': 100,
  'A': 'string',
}
print(dict2) # Output: {'A': 'string'}

# The values of the dictionary can be used separately from the keys with the values() method
print(dict1.values()) # Output: dict_values([100, 'string', [1, 2, 3]])

# The items of the dictionary can be used separately from the keys with the items() method
print(dict1.items()) # Output: dict_items([('A', 100), ('B', 'string'), (1, [1, 2, 3])])

# The length of the dictionary can be obtained using `len()`
print(len(dict1)) # Output: 3
# `len()` can also be combined with the two methods mentioned above (and more!)

# Dictionaries can be converted into lists/tuples
print(list(dict1)) # Output: ['A', 'B', 1] - notice that it only prints the keys
print(tuple(dict1)) # Output: ('A', 'B', 1) - notice that it only prints the keys

# Dictionaries can also be converted into strings
print(str(dict1)) # Output: {'A': 100, 'B': 'string', 1: [1, 2, 3]} - again, it looks like a dictionary but it IS a string

# Indexing doesn't work with dictionaries
# Instead, the key is used to return the value of the key
print(dict1['A']) # Output: 100 - note that the key is case-sensitive... `dict1['a']` would not work

# The `get()` method can also be used to retrieve a key's value from a dictionary
print(dict1.get('X')) # Output: None
# Returns a null value because the key doesn't exist unlike `print(dict1['X'])` which would crash

# Key-value pairs can be added like most programming languages
dict1['C'] = 1 # Using the `update()` method also works: `dict1.update('C' = 1, 'D' = 2)` or `dict1.update({'C' = 1, 'D' = 2})`
print(dict1) # Output: {'A': 100, 'B': 'string', 1: [1, 2, 3], 'C': 1}
