# Input and pass

'''
Input is a way to get a user input, although rarely used.

Pass tells Python to not do anything. This can be added to a function if there is
no code written for the function yet.
'''

# User input can be obtained via the `input()` function
# An argument can be passed into the function to tell the user what to input
user_input = input('Type your name: ')

# Once the user input has been received, it will be stored in the variable

# Here is a function that needs to be written but doesn't have any content yet
# If the function is left empty, Python will throw an error, so add `pass` to it
def important_function():
  pass # No more errors!
