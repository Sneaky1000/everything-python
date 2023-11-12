# Sorting data

'''
Functions can be passed into another function as an argument. The best example of this
is the `sorted()` function. This function 
'''

# Numbers will be sorted in ascending order
original_nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(sorted(original_nums)) # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# Characters/letters will be sorted in alphabetical order
original_string = 'hello'
print(sorted(original_string)) # Output: ['e', 'h', 'l', 'l', 'o']

# There are also parameters. This example uses the `reverse` parameter to reverse the sort order of `original_nums`
print(sorted(original_nums, reverse = True)) # Output: [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]

# Custom keys can be provided for the `key` parameter to tell the sort function what to sort by
original_words = ['apple', 'blueberry', 'grape', 'kiwi', 'strawberry']
print(sorted(original_words, key = len)) # Output: ['kiwi', 'apple', 'grape', 'blueberry', 'strawberry']

# The `key` can also be a custom function

# Example list of tuples to be sorted...
list_of_tuples = [('a', 3), ('b', 10), ('c', 5), ('d', 21), ('e', 14)]

# Define how to sort the list of tuples...
def sort_func(item): # Each tuple is passed into the function as `item`
  return item[1] # The return should be a number that tells `sorted()` what to look for when sorting

# Since `sort_func()` returns the second value in each tuple, it will sort by the second value
print(sorted(list_of_tuples, key = sort_func)) # Output: [('a', 3), ('c', 5), ('b', 10), ('e', 14), ('d', 21)]

# The last example can be shortened using a lambda function
print(sorted(list_of_tuples, key = lambda item: item[1])) # Output: [('a', 3), ('c', 5), ('b', 10), ('e', 14), ('d', 21)]
