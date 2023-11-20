# `eval()` and `exec()`

'''
Both `eval()` and `exec()` are functions inside of Python. What makes them special
is that they translate strings into Python code. From operations such as addition
all the way to creating new variables from a string are possible using these functions.

! IMPORTANT: BE EXTREMELY CAREFUL WHEN USING EITHER OF THESE FUNCTIONS !

If handled poorly, external users can run THEIR OWN CODE inside the ORIGINAL CODE.

Example: A user can use an input field that employs `eval()` or `exec()` to run malicious
scripts that could completely steal or delete all database records.

With that out of the way, let's start with `eval()`.

`eval()` is the weaker of the two. It can only evaluate code. This means that it can run
functions and simple operations but it cannot create new variables or things of that nature.

So what does `exec()` do?

`exec()` is the more powerful function. It can execute any code. It can create variables,
run functions, etc.

'''

# Simple example of `eval()`
print(eval('"test".upper()')) # Output: TEST

# Essentially, what is happening is that `eval()` is removing the single/double quotes and
# running the code just as if it were written like normal Python code

# `eval()` has a lot of limitations. `if` statements will not work. This is where `exec()`
# comes into play...
exec('if True: print("test")') # Output: test

# `eval` cannot set variables or create them... but `exec()` can
a = 10

exec('a = 2')

exec('b = 1')

print(a) # Output: 2
print(b) # Output: 1

# Example of a use case: print the word 'test' in all uppercase, all lowercase, titlecase, and casefold
# This is EASY with `eval()` and `exec()`...
my_string = 'tEsT'

for op in ['upper', 'title', 'lower', 'casefold']:
  print(eval(f'my_string.{op}()'))
'''
Output:

TEST
Test
test
test
'''
