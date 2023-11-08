# Sets

'''
Sets are similar to dictionaries but don't have keys. They are special
because each value must be unique and all duplicates are deleted.
'''

# Example of a set removing duplicates
set1 = { 1, 2, 3, 3, 3, 4, 4 }
print(set1) # Output: {1, 2, 3, 4}

# There are plenty of methods to attach to a set just like all other variables
# Some are shown below (see 'methods.py' in the 'basics' folder for more details)
set1.add(5) # Adds '5' to the end of the set
set1.remove(5) # Removes '5' from the set

# The length of the set can be obtained using `len()` but indexing and slicing is not available for sets
print(len(set1)) # Output: 4

# Sets are great when it comes to comparisons (methods are shown below along with the shortcut syntax)

# The `union()` method can be used to take two sets and create a new set with the combined elements
set_a = { 1, 'A', 2, 'B' }
set_b = { 1, 'C', 2, 'D' }
print(set_a.union(set_b)) # Output: {1, 2, 'C', 'A', 'D', 'B'}
print(set_a | set_b)      # Output: {1, 2, 'C', 'A', 'D', 'B'}

# The `intersection()` method can be used to create a new set with elements only present in both sets
print(set_a.intersection(set_b)) # Output: {1, 2}
print(set_a & set_b)             # Output: {1, 2}

# The `difference()` method can be used to get the elements that are present in the set the method is attached to
# but not present in the set put in the argument
print(set_a.difference(set_b)) # Output: {'A', 'B'}
print(set_b.difference(set_a)) # Output: {'C', 'D'}

print(set_a - set_b)           # Output: {'A', 'B'}
print(set_b - set_a)           # Output: {'C', 'D'}

# Other notes
# -----------
# 1. Indexing can be done on sets by converting the type to something indexable
