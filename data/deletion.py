# Deletion

'''
Python uses the `del` keyword to delete things.

`del` can delete variables (though that is rare), values from lists, dictionaries, etc.
'''

# Deleting a variable
a = 1
del a

# Now, attempting to print `a` will throw an error

# Removing items from a list - `del` removes values by index
a = [1, 2, 3]
del a[0]
print(a) # Output: [2, 3]

# There is also the `remove()` method, which removes by VALUE, not by index
a.remove(3)
print(a) # Output: [2] - remember that '1' was deleted earlier

# The `pop()` method also removes values by INDEX, but the default index is -1
# It's used to remove the last value of the list ('stack' data structure *wink* *wink*)
b = [1, 2, 3]
b.pop()
print(b) # Output: [1, 2]

# The `clear()` method deletes all values from the list
b.clear()
print(b) # Output: []
