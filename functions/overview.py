# Functions overview

'''
A function is simply a block of code that can be reused. It works just like
any other language. Functions must be 'called' in order to run. Functions
can even be customized in terms of when they're called. (ex. using a loop to
call the function repeatedly).
'''

# Functions are defined using the 'def' keyword
def my_function():
  print('Hello, world.')
  res = 1 + 2
  print(res + 1)

# Functions can be called (multiple times) like this:
my_function() # Run the function once
my_function() # Run the function again
# Output: Hello, world. \ 4 \ Hello, world. \ 4

# Functions can take in arguments by adding parameters:
def simple_calc(num1, num2):
  return num1 + num2

print(simple_calc(3, 10)) # This runs the function and passes the number 3 in for num1 and 10 for num2
# Output: 13

'''
Notice how `my_function()` had no `return` whilst `simple_calc()` did. Not adding a return in a
function doesn't mean the function doesn't return anything. It's the same as returning `None`.
HOWEVER, that value is not meant to be used. Returning values is somewhat similar to how `break`
works. However, returning any value stops the function execution at that point and give the returned
value as an output to be used in some other part of the code. `simple_calc()` in the example above
returns 13 when given the arguments 3 and 10. That value is then returned, and since the function is
is being called inside a print() function, it prints 13 to the console/terminal. See 'parameters.py'
in the 'functions' folder for more information.
'''

