# Creating custom modules

'''
Why create custom modules? Organization. Each module can be put in a separate file
so there is never too much in one file.
'''

# Import 'my_module.py' from the 'custom_modules' folder
from custom_modules import my_module

# Print the variable inside the `my_module.py` file
print(my_module.test_string) # Output: Hello, world!

# Create an object using the `TestClass` in the `my_module.py` file
testObject = my_module.TestClass(name = 'Chase')

# Run the `say_hello` method from the `TestClass`
testObject.say_hello() # Output: Hello, Chase!
