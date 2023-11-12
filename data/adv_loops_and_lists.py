# Advanded loops / list manipulation

'''
A common practice involves merging lists and subsequently iterating
over the combined result. An elegant approach in Python is to zip the lists together
and assign an index to each element within a for loop. This permits more concise
and a more readable way to traverse multiple lists simultaneously.
'''

# Example of two lists that need to be merged and iterated over to get a result
# Practicality: Excel sheet columns and rows of products and their inventory are extracted
# Those extracted lists often look like this:
inventory_items = ['Apples', 'Bananas', 'Strawberries', 'Grapes', 'Melons']
inventory_quantities = [43, 12, 84, 16, 27]

# There are 43 apples, 12 bananas, 84 strawberries, etc. (based on position/index)

# The built-in function `zip()` takes two arguments (iterables such as lists)
# It then creates pairs by taking the corresponding elements from each iterable
# and bundling them together
zipped_pairs = zip(inventory_items, inventory_quantities)
print(zipped_pairs) # Output: <zip object at 0x7f1ce7994200> - (A zip object at memory address 0x7f1ce7994200)

# Printing this without converting it to a list will not print the expected content
# It won't print the expected output because `zip()` returns an iterator object, not a list

# Use list() to convert the pairs into a list of tuples
inventory = list(zipped_pairs)
print(inventory) # Output: [('Apples', 43), ('Bananas', 12), ('Strawberries', 84), ('Grapes', 16), ('Melons', 27)]

'''
Note that this is NOT required to use the zipped lists! `zip()` can be iterated over as long as it isn't assigned
to a variable. This is due to the fact that `zipped_pairs`, for example, holds a REFERENCE to the iterator.
When you try to iterate over zipped_pairs, it goes through the iterator once. After the first iteration, the iterator is 
exhausted, and attempting to iterate over it again will result in an empty sequence because the iterator has reached its end.
If you want to iterate over the pairs more than once, you should recreate the iterator. You can do this by calling zip() again
or by converting it to a list
'''


# This for loop combines `inventory_items` and `inventory_quantities` into pairs
# It then unpacks each pair into the variables `item` and `quantity`
# The first variable, `item`, iterates over inventory items, while `quantity` over inventory quantities
# These are then used to print each item and its respective quantity
for item, quantity in zip(inventory_items, inventory_quantities):
  print(f'Item: { item } | Quantity: { quantity }')
'''
Output:

Item: Apples | Quantity: 43
Item: Bananas | Quantity: 12
Item: Strawberries | Quantity: 84
Item: Grapes | Quantity: 16
Item: Melons | Quantity: 27
'''

# Q: What if the index of the inventory names needs to be known?
# A: The built-in function `enumerate()` gets the current index of each item in an iterable

# `enumerate()` is similar to `zip()` in that it returns an iterator object
print(enumerate(inventory_items)) # Output: <enumerate object at 0x7f04e9394540> - (An enumerate object at memory address 0x7f04e9394540)

# Just like `zip()`, it can be converted into a list to get the expected output
print(list(enumerate(inventory_items))) # Output: [(0, 'Apples'), (1, 'Bananas'), (2, 'Strawberries'), (3, 'Grapes'), (4, 'Melons')]

# Now, each item and its respective index can be printed by iterating over the enumerated `inventory_items`
for index, item in enumerate(inventory_items):
  print(f'{ index }: { item }')
'''
Output:

0: Apples
1: Bananas
2: Strawberries
3: Grapes
4: Melons
'''

# Other notes:
# ------------
# 1. `range()` is also commonly used when handling data via iteration. (see 'loops.py' in the folder 'flow' for more information)
