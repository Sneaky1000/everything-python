# __main__

'''
When a Python file is called, it creates a few internal variables. The most used
internal variable is `__main__`. Essentially, it gives a name to the current Python
file. The one being executed is always `__main__`. Imported files are called `__name__`
where 'name' is the name of the file being imported.
'''

# Import 'my_module.py'
from custom_modules import my_module

# Printing the name of this file as well as the name of the imported file
# Imports come first, then the name of the main file that is being executed
print(__name__) # Output: custom_modules.my_module \ __main__
