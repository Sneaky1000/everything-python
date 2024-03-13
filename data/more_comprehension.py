# More comprehension

'''
IMPORTANT: See 'list_comprehension.py' in the 'data' folder first!

Besides list comprehension, there is also dictionary comprehension,
tuple comprehension, and set comprehension.

Dictionary comprehension syntax (using `num` as the appended value):
{num: num for num in range(x)}

Set comprehension syntax (using `num` as the appended value):
{num for num in range(x)}

Tuple comprehension syntax (using `num` as the appended value):
tuple(num for num in range(x))

* Notice how tuple comprehension is the same as list comprehension
  but now it is being converted manually.

This file will not go over comprehension as in depth as the 'list_comprehension.py'
file does in the 'data' folder because the only main difference is the syntax.
'''

# Dictionary comprehension example
dict_comp = {num: (num**2) for num in range(5)}
print(dict_comp) # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension example
set_comp = {num for num in range(10)}
print(set_comp) # Output: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


# Tuple comprehension example
tuple_comp = tuple(num for num in range(8))
print(tuple_comp) # (0, 1, 2, 3, 4, 5, 6, 7)
