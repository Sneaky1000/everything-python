# Scope

'''
Scope cope refers to the region of code where a variable or function is accessible.
It defines where in the program a particular identifier (like a variable or function)
can be used or modified.
'''

# In Python, variables created inside of a function are only accessible inside that function
# This is called 'local scope'
def test1():
  local_var = True # This variable can only be accessed from inside `test1()`
  print(local_var)
test1() # Output: True

# Another function can be made using `local_var` as a variable but it will be an entirely new variable
# (It would be the equivalent of creating a brand new variable)

# _variables created outside of a function are considered 'global scope' and can be accessed anywhere
# However, global variables defined outside of a function cannot be changed
global_var = 2 # Trying to use `global_var += 1` inside a function will error because this variable is not editable

# Global variables can be created inside of a function via the 'global' keyword
# (See 'variables.py' in the 'basics' folder for more information)
def test2():
  global test_var # Global variable `test_var` is defined inside of a function
  test_var = 100 # It is then initialized

  print(global_var)

# Here, the global variable created in `test2()` is printed to the console/terminal
def test3():
  print(test_var)

test2() # Output: 2
test3() # Output: 100

# Returning a variable in a function can transform it from being local to being global
# This example uses parameters to do this (`a`) - `a` is considered a local variable because it's a parameter
# that can only be accessed within the function
def test4(a):
  a += 1
  return a

# The value of `a` via the 'return' can then be reassigned to a variable or used directly
b = test4(2)
print(b) # Output: 3
print(test4(2)) # Output: 3

# Other notes
# -----------
# 1. It is generally bad to use the 'global' keyword, so try to avoid it
