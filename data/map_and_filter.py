# Sorting data via map and filter

'''
Though map and filter have mostly been replaced by list comprehension, they are
still good to know as they may come up ocassionally.

`map()` changes values with a function inside an iterable
`filter()` filters out values given a condition
'''

# Example of `map()` - Map takes value from an iterable and returns a new iterable with the changes
# So, instead of sorting it, `map()` changes every value and returns a new iterable
my_list = [1, 2, 3, 4, 5]

# Function `power_func()` takes a value and multiplies it by its itself
def power_func(num):
  return num ** 2

# Now attach the function to `map()` and give it the list of values to be mapped
# Similar to `zip()` and `enumerate()`, printing this will return an iterator object, not a list
print(map(power_func, my_list)) # Output: <map object at 0x7efec0763ac0>

# Convert the iterator object to a list to see the result
print(list(map(power_func, my_list))) # Output: [1, 4, 9, 16, 25]

# This example can be shortened using a lambda function
print(list(map(lambda num: num ** 2, my_list))) # Output: [1, 4, 9, 16, 25]

# Example of `filter()` -Filter takes a key and an iterable for arguments
# Filter takes an iterable and returns a new iterable with the values that match the condition

# This function returns `True` if the number is less than four, `False` otherwise
def below_4_func(num):
  return num < 4

# Pass `filter()` the condition and the iterable...
# (Remember: printing without converting to a list will return the iterator object)
print(filter(below_4_func, my_list)) # Output: <filter object at 0x7fb33545bee0>
print(list(filter(below_4_func, my_list))) # Output: [1, 2, 3]

# And just like the example for `map()`, this example can be shortened using a lambda function
print(list(filter(lambda num: num < 4, my_list))) # Output: [1, 2, 3]
