# List comprehension

'''
List comprehension is a way to create lists on a single line of code. It can be used
to create simple lists or manipulate existing lists. See the example below for the syntax
'''

# Regular list creation with a loop (list of integers 0 to 99)
list1 = []

for num in range(0, 100): # From 0 to 99...
  list1.append(num) # Append each number to the list

# List creation via list comprehension (list of integers 0 to 99)
list2 = [num for num in range(0, 100)] # The first `num` is the value that will be appended to the list
#           [                         ] <-- This space above (and inside) this bracket is the exact same

# Q: What if the list needs to contain tuples of two differnt values - (0 to 9, 10 to 19)?
# A: Add a tuple that contains two values before the expression
list3 = [(num, num + 10) for num in range(0, 10)]
print(list3) # Output: [(0, 10), (1, 11), (2, 12), (3, 13), (4, 14), (5, 15), (6, 16), (7, 17), (8, 18), (9, 19)]

# List comprehension can be combined with a ternary operator to make more complex expressions
# The conditional for the ternary operation must come BEFORE the list comprehension if using both `if` and `else` because 
# `else` does not work if written the other way around
# Otherwise, the conditional must come AFTER the list comprehension if only using `if`

# For each `num` from 0 to 14, append `num` to `list4` if `num` < 10. Otherwise, append 0 instead
list4 = [num if num < 10 else 0 for num in range(0, 15)]
print(list4) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0]

# List comprehension + ternary operators are frequently used to filter lists
inventory_items = ['Apples', 'Bananas', 'Strawberries', 'Grapes', 'Melons']
inventory_quantities = [43, 12, 84, 16, 27]

# If the item has a quantity less than 30, it will be added to the restock list
restock_list = [(item, quantity) for item, quantity in zip(inventory_items, inventory_quantities) if quantity < 30]
print(restock_list) # [('Bananas', 12), ('Grapes', 16), ('Melons', 27)]

# List comprehension can be combined/nested

# This list comprehension is printing a list from 0 to 4 as the loop increments from 0 to 9
combined_comp = [[x for x in range(5)] for _ in range(10)]

# Printing each `row` out makes it look like a matrix (data structures and Leetcode will remember this...)
for row in combined_comp:
  print(row)
'''
Output:

[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
'''

# If `_` from combined_comp is moved inside the append and added as `y` to make the append a tuple...
combined_comp2 = [[(x, y) for x in range(5)] for y in range(10)]

'''
In the matrix above, for each column in each row, the value of `x` increments by +1 from 0 to 4.
For each row, the value of y increments by +1 from 0 to 9. Then, those two values are appended
via a tuple as (x, y).
'''


# Printing it as a matrix makes it easier to understand
for row in combined_comp2:
  print(row)
'''
Output:

[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)]
[(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)]
[(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)]
[(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
[(0, 5), (1, 5), (2, 5), (3, 5), (4, 5)]
[(0, 6), (1, 6), (2, 6), (3, 6), (4, 6)]
[(0, 7), (1, 7), (2, 7), (3, 7), (4, 7)]
[(0, 8), (1, 8), (2, 8), (3, 8), (4, 8)]
[(0, 9), (1, 9), (2, 9), (3, 9), (4, 9)]
'''
