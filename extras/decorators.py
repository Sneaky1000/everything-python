# Decorators

'''
Warning: This is a much more advanced topic compared to the rest of the topics learned so far.

Decorators are functions that 'decorate' other functions. It's essentially the process of
wrapping one function around another function. What does this do? This allows functions to
have extra functionality without changing it. For example, a decorator can be made for a 
function that makes the function execute twice when called. 

For more advanced developers,the topic of 'recursion' will come to mind when hearing this. 
However, this will not be discussed in this project due to the complexity of it's nature.

So, when is this useful?

There are typically three circumstances where decorators are used:
  1. To test code without changing it.
  2. Trying to avoid unnecessary changes in code when working in a team.
  3. To run code when a class's attributes are modified or accessed.
'''

# Import modules for later examples
import time

# Firstly, a recap on functions

# Here is a function that prints a string
def inner_func():
  print('Inner function')

# This function taks a function in as an argument and runs it
def wrapper_func(function):
  print('Calling function...')
  function()

# Now, call `wrapper_func()` and pass `innder_func()` as an argument without calling it
wrapper_func(inner_func) # Output: Calling function... \ Inner function

# Functions can be created inside a function
def func_generator():
  def new_function():
    print("New function")
  return new_function

# Call the `func_generator()` function and assign its return value to `new_func`
new_func = func_generator()

# Calling `new_func` will now run `new_function()` inside `func_generator()`
# This is because new_func was assigned to the called `func_generator()` which
# returned `new_function` - so `new_func` = `new_function`
new_func() # Output: New function

# By calling `new_func()` it is calling `new_function()`

# Separator for clarity
print('----------------------------------------------------------------')

# Let's try a more complex example using the `@` shorthand
def decorator(func):
  print('Outside the wrapper')
  def wrapper():
    print('Decoration begins...')
    func()
    print('Decoration ends...')
  
  return wrapper

# By adding the @decorator shorthand above `test1`, it is passing this function to `decorator()` as an argument
@decorator
def test1():
  print('Test1 has been ran')

# Now, by calling `test1()`, it is calling `decorator(test1)` and the returned function `wrapper` inside `decorator`
test1()
'''
Output:

Outside the wrapper
Decoration begins...
Test1 has been ran
Decoration ends...
'''

# Separator for clarity
print('----------------------------------------------------------------')

# Decorators can be added on top of each other to combine them
# Let's say `decorator()` from the previous example is decorator 1
# Now, decorator 2 will be defined below. It sleeps for 1 second and
# prints the duration that it slept for...
def duration_decorator(func):
  def wrapper():
    start_time = time.time()
    func()
    duration = time.time() - start_time
    print(f'Duration slept: {duration}')
  return wrapper

@decorator # Calls `decorator()`
@duration_decorator # Calls `duration_decorator()`
def test2():
  print('Test2 running...')
  time.sleep(1) # Sleep for 1 second

# Calling `test2()` calls `decorator(test2)` and the returned `wrapper()` function
# Then it calls `duration_decorator(test2)` and the returned `wrapper()` function
test2()
'''
Output:

Outside the wrapper
Decoration begins...
Test2 running...
Duration slept: 1.0010192394256592
Decoration ends...
'''

# Separator for clarity
print('----------------------------------------------------------------')

'''
IMPORTANT: Functions with parameters can be decorated!
'''

# The most common type of parameter set is the (*args, *kwargs) parameters
# This allows the decorator to take in any function as the arguments can be anything
def decor_func(func):
  def wrapper(*args, **kwargs): # `*args` deals with lists, `*kwargs` deals with dictionaries
    print('Decoration begins...')
    func(*args, **kwargs) # This function's arguments MUST match the wrapper parameters
    print('Decorator ends...')

  return wrapper

@decor_func
def func(func_param):
  print(func_param)

func('a string')
'''
This time, instead of passing a static string such as 'Test2 running...' like in the previous 
example, `func` is taking in a parameter that is printed with the decorator function wrapping it.
'''

# Separator for clarity
print('----------------------------------------------------------------')

'''
IMPORTANT: Decorators themselves can have parameters!
'''

# Goal: Print the string from `test3` (defined further below) five times

# Decorator that takes in the number of repetitions as an argument
def repetition_decorator(repetitions):
  def decorator(func):
    def wrapper():
      # For each repetition desired...
      for _ in range(repetitions):
        func() # Run the function passed as an argument
    return wrapper
  return decorator

@repetition_decorator(5)
def test3():
  print('A string from test 3')
  
test3()

'''
Output:

A string from test 3
A string from test 3
A string from test 3
A string from test 3
A string from test 3
'''

'''
Explanation: This is simply a decorator with one extra wrapper function called `repetition_decorator`.
The only difference is that the outer-most decorator takes in a number argument that gets passed to the
inner-most `wrapper` function. All the outer-most decorator does is take in an argument, then move inward
to the returned `decorator` function, which then takes the function passed as an argument and runs it 5 times
before exiting.
'''

# Separator for clarity
print('----------------------------------------------------------------')

# Now, for decorators in classes...

# It's important to understand the `@property` shorthand (comes from the `property()` function)
# This allows methods to be turned into attributes
# property()takes in a getter, setter, and deleter like this: `property(getter, setter, deleter)`
# Getter is called when viewing the attribute
# Setter is called when modifying the attribute
# deleter is called when deleting the attribute

# Example...
class Generic:
  # Set attributes
  def __init__(self):
    self._x = 10 # Set `x` as a private attribute
  
  # Define getter method
  def getter(self):
    print('Getting x...')
    return self._x
  
  # Define setter method
  def setter(self, value):
    print('Setting x...')
    self._x = value
  
  # Define deleter method
  def deleter(self):
    print('Deleting x...')
    del self._x
  
  # Use "public" `x` because this is what's being accessed outside the class
  x = property(getter, setter, deleter)

generic = Generic()
print(generic.x) # Output: Getting x... \ 10
generic.x = 2 # Output: Setting x...
# Get the new value of `x`
print(generic.x) # Output: Getting x... \ 2
del generic.x # Output: Deleting x...

# This isn't a very elegant way of writing this though...
# Here is the same class re-written uing`@property` instead of `property()`

# First, let's separate the outputs with a line
print('----------------------------------------------------------------')

class Generic2:
  # Set attributes
  def __init__(self):
    self._x = 10 # Set `x` as a private attribute
  
  @property
  def x(self):
    print('Getting x...')
    return self._x
  
  @x.setter
  def x(self, value):
    print('Setting x...')
    self._x = value
  
  @x.deleter
  def x(self):
    print('Deleting x...')
    del self._x

generic2 = Generic2()
print(generic2.x) # Output: Getting x... \ 10
generic2.x = 2 # Output: Setting x...
# Get the new value of `x`
print(generic2.x) # Output: Getting x... \ 2
del generic2.x # Output: Deleting x...
