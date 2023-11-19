# Modules overview

'''
Modules are extra parts that can be attached to programs For example, how about
a random number generator? This can be added via the `random` module. Modules
can also be created manually (across multiple files) to better organize code.

Importing modules:
  1. Modules can be imported from the Python standard library (these come 
     pre-installed with Python).
  2. Modules can be made by other users and imported but these need to be
     installed manually before using.
     
This overview will go over the Python standard library to learn the fundamental
concepts of modules before diving into external modules and manually-created modules.
'''

# Import the random module
import random

# If only one feature of a module is needed, just import that feature
from math import floor

# Imports can also be renamed
from math import ceil as ceiling

# Modules can be imported with the `*` to import everything from the module
# This allows functions to be used from the module without having to add the
# module name before the function name:
from string import *

# An infinite number of modules can be imported
# When importing modules, they can be put on the same line using a comma if desired:
# import string, random, ...

# Now, to use the `random` module, see this syntax:
# module_name.function(args...)
# Here, the function randint(min, max) is being used to generate a random number
# between 0 and 10
random_number = random.randint(0, 10)
print(random_number) # Output is any number between 0 and 10 inclusive

# So how is information on a module found? Google!
# Here is the `random` module documentation (link to `randint()` function specifically):
# https://docs.python.org/3/library/random.html#random.randint

# Here is another example
test_list = [None, 'hello', 3.1, 4, True]
print(random.choice(test_list)) # Outputs a random element from `test_list`

# Using `floor()` from the `math` module
print(floor(4.8)) # Output: 4

# Using `ceil()` as `ceiling()` from the `math` module
print(ceiling(2.1)) # Output: 3

# Because all the functions from the `string` module were imported with the `*`
# `ascii_lowercase` can be used without needing `string.` in front
print(ascii_lowercase) # Output: abcdefghijklmnopqrstuvwxyz





