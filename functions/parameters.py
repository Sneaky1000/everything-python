# Parameters

'''
When a functtion is created, parameters can be set. Arguments can be assigned
to the parameters. Parameters can then be used like variables inside the function.
When calling a function, arguments can be added to give the parameters values.
Arguments are assigned to parameters by their position in the function by default.
Keyword arguments can be used to be more precise.
'''

# Example of parameters in a function
def test_func(a, b, c):
  print(a)
  print(b)
  print(c)

# In this callback, 1 is being assigned to `a`, 'hello' to `b`, and the list to `c`
test_func(1, 'hello', [5, '10', True]) # Arguments passed to the parameters by position
# Output: 1 \ hello \ [5, '10', True]

# In this callback, 2 is being assigned to `b`, 1 to `a`, and 3 to `c`
test_func(b = 2, a = 1, c = 3) # Arguments passed to the parameters via keyword arguments
# Output: 1 \ 2 \ 3

# Both keyword arguments and position arguments can be combined...
# HOWEVER, position arguments MUST COME FIRST or the Python will error out
test_func(1, c = 3, b = 2) 
# Output: 1 \ 2 \ 3

# Parameters can also be given default arguments to use if they are not defined on the callback
def func2(x, y = 1):
  print(x)
  print(y)
  
# Now, when func2() is called without a `y` argument defined, it will default to 1
func2(5)
# Output: 5 \ 1

# Q: What if the number of arguments is unknown?
# A: Use the unpacking operator to combine the arguments into a tuple that can be iterated on
def func3(*args): # The '*' operator will unpack the arguments passed into the function (turn them into a tuple)
  for arg in args:
    print(arg)

# Now, infinite number of arguments can be passed and the function will handle them
func3(1, 2, 3, 'test', True, None) # The unpacking operator in the function will take these arguments and convert them into a tuple
# Output: 1 \ 2 \ 3 \ test \ True \ None

# Q: What if there is one argument guaranteed to be in the function but the rest are unknown?
# A: Create two parameters. One parameter without the unpacking operator, the other with it
def func4(arg1, *extraArgs):
  print(arg1)
  print(extraArgs)

# This callback will send the first argument as `arg1`, and any others to the right as `extraArgs`
func4(1, 5, 10, 15)
# Output: 1 \ (5, 10, 15)

# Important note: If another parameter was added after `extraArgs` in `func4()`, keyword arguments would be required.
#                 Position arguments wouldn't be usable as all arguments after the first would be considered part of 
#                 `extraArgs`.

# Unpacking twice '**' will take the arguments and turn it into a dictionary
def func5(**args):
  print(args)

# The name of the argument variable will be the key, while the value will be the value of the key
func5(num1 = 1, num2 = 2) # Keyword arguments are REQUIRED as they are used as the keys of the dictionary
# Output: {'num1': 1, 'num2': 2}
