# Exceptions / error handling

'''
Obviously, code should not contain any errors as that would crash the program.
However, sometimes, performing certain operations will cause unexpected errors.
For that, Python has tools to anticipate errors and deal with them without
crashing the program. Error handling is extremely common when paired with asynchronous
programming which will not be covered in this file because it's a more advanced topic.
'''

# This example will use dividing by zero as the error
# Dividing by zero will obviously cause an error when executing
# This is where try/except is used - whenever there might be an error
try: # Python will try executing the code in this block
  print(1/0)
except Exception as err: # If it fails or errors out, it will execute the code in this block
  # Python catches the exception message using the general keyword `Exception` renamed to `err` and prints the message
  print(err) # Output: division by zero

# Error handling can be made to be more specific...
# Pay attention to the execution order
try: # Python will try executing the code in this block
  print(non_existant_variable) # This is the first error so this block will stop being executed
  print(1/0) # Doesn't get executed because of the error above
except NameError: # Python sees this error matches the executed code's error
  print('Variable name not found / does not exist') # Instead of crashing, it prints this string and exits
except ZeroDivisionError: # This is never reached as a result
  print('Cannot divide by zero')

# `finally` can be used to run code no matter what after the error has been handled
try: # Try executing the code in this block
  print(1/0) # ZeroDivisionError occurs
except ZeroDivisionError: # Error matches
  print('Cannot divide by zero') # Print this string
finally: # Now that the error has been handled...
  print('An error has occured') # Print this string

# Error/exceptions can be created manually with the `raise` keyword
# This example uses `isinstance()` which checks if a value matches a datatype
must_be_string = 12

# If the variable's value is a string, print the string
if (isinstance(must_be_string, str)):
  print(must_be_string)
# Otherwise, raise an error
else:
  # The exception `TypeError` is raised with the custom message 'Value must be a string'
  # Note that this will cause the program to crash
  raise TypeError('Value must be a string') # Output: TypeError: Value must be a string

# There is also the `assert` keyword which checks if a value passes a conditional statement
# If it doesn't pass the check, it will crash the program
# (Note: Comment out the `raise` code above to see this code work)
a = 5

assert (a == 10) # Output: AssertionError
