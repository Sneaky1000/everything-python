# Methods

# Python has various built-in methods dependant on the type of object
# All methods can be found below in the 'Other notes' section
# This file will only go over a few of these methods

# upper() converts a string into uppercase
test1 = 'a random string'.upper()
print(test1) # Output: A RANDOM STRING

# title() converts the first character of each word to uppercase
test2 = 'a RANDOM sTriNg'.title()
print(test2) # Output: A Random String

# dir() returns all the properties and methods valid for the specified object, even built-in properties which are default for all objects
test3 = 'test'
print(dir(test3)) # Output is too long (run the code to see the '__properties__' and 'methods()')

# Other notes
# -----------
# 1. All string methods: https://www.w3schools.com/python/python_ref_string.asp
# 2. All list methods: https://www.w3schools.com/python/python_ref_list.asp
# 3. All dictionary methods: https://www.w3schools.com/python/python_ref_dictionary.asp
# 4. All tuple methods: https://www.w3schools.com/python/python_ref_tuple.asp
# 5. All set methods: https://www.w3schools.com/python/python_ref_set.asp
# 6. All file mthods: https://www.w3schools.com/python/python_ref_file.asp
