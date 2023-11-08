# Booleans

'''
Booleans are extremely common and are the return value for many comparisons.
All comparison operators are allowed in Python (==, !=, <=, >=, <, >).
'''

# Example: is 1 equal to 1?
print(1 == 1) # Output: true

# Example: is 1 not equal to 1?
print(1 != 1) # Output: false

# Lists, tuples and strings can be check to see if they contain a specific value using the `in` keyword
print(1 in [1, 2, 3]) # Output: true
print('e' in 'hello world') # Output: true
print(5 in (1, 2, 3)) # Output: false

# Booleans can be used by themselves without a comparison operation
print(True) # Output: true - notice the argument is capitalized because it's printing a data type (similar to `None`)
print(not True) # Output: false

# Dictionaries and sets can also be checked to see if they contain a specific value
dict1 = {
  1: 'one',
  2: 'two',
  3: 'three',
}
print(1 in dict1) # Output: true
print('one' in dict1) # Output: false - remember that values are not accessible unless specified explicitly
print('one' in dict1.values()) # Output: true
print('four' in dict1.values()) # Output: false

# The `bool()` function accepts any number, string, type of container, etc and still returns a value
# There are rules that make values either 'truthy' (values that are converted to true) or 'falsy' (values that are converted to false)

'''
Falsy values:
  0 or 0.0 or 0.0000... (int and float)
  '' or "" (empty string)
  [], (), {} (empty list, tuple, set, dictionary)
  None (absence of a value)
  
Truthy values:
  Literally anything else
'''

print(bool(123124523)) # Output: true
print(bool('')) # Output: false
