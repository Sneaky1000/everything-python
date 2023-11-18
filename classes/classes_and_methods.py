# Classes and methods

'''
Everything in Python is an object. This includes the in-built strings, integers, etc.
Even functions are objects. Now, methods. A function and a method both execute a block
of code. The difference is that a method always belongs to an object.
'''

# Now that it's understood that everyhing in Python is an object,
# Here is an example of a function vs a method
print(len('test')) # Output (of the function): 4
print('test'.upper()) # Output (of the method): TEST


# Everything being an object also means that there are built-in methods for every data type
# Here is a string. Using `dir()` on the string shows all the built-in methods that can be used
# on this object
test1 = 'some string'

print(dir(test1))
'''
Output (all one line): 
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
'__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode',
'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix',
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
'''

# Objects can be passed into classes (for example, functions)
def add(a, b):
  return a + b

class Test:
  def __init__(self, add_func):
    self.add_func = add_func # Store the passed-in addition function as an attribute

# It's important to not call the `add()` function, but rather pass the function OBJECT instead
test = Test(add_func = add)

# Printing this 'test' object with the attribute `add_func` and passing two numbers as arguments will now add them together
print(test.add_func(2, 3))

