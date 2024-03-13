# If, elif, else

'''
'If (`if`) statements' only run code when a condition is satisfied. They work just like
every other programming language and can be extended with else if (`elif`) as well
as else (`else`). These statements can be nested and/or combined to make more complex
conditions to alter the flow of the code's execution.
'''

# Multiple lines of code can be ran inside an if statement (change the variable values to get different outputs)
x = 7
y = 10

if x > 10:
  print('The if statement condition has been satisfied')
  print('More than one line of code can be ran when a condition is met!')
elif x == 7:
  print('First condition wasn\'t satisfied, but the second condition was!')
  y += 1
  print(f'Also increment y by +1 when this condition is met to get y = {y}!')
else:
  print('No condition was satisfied so this is the default output')


# Using if `x` and if not `x` can check if a value is truthy or not (see example below)

# Combining conditions (and, or) and nesting statements is simple
a = 'string'
b = None
c = 4

if not a: # If `a` is falsy...
  print('`a` is a falsy value')
elif a and b: # If `a` and `b` are truthy...
  print('Both `a` and `b` are truthy values')
elif not a and not b: # If `a` and `b` are falsy...
  print('`a` and `b` are falsy')
elif a: # If `a` is truthy...
  print('`a` is truthy...')
  if not b: # check if `b` is falsy...
    print('and `b` is falsy')
elif a == 4 or b == 4 or c == 4: # If `a` or `b` or `c` is equal to 4...
  print('Either `a`, or `b`, or `c`, or all, are equal to 4')
  # This will never run even though `c` = 4 because the condition above is already met
  # (If statements end when a condition is met)
else:
  print('No condition was met')
# Output: `a` is truthy... \ and `b` is falsy

# One thing to quickly mention is that Python has ternary operations
# Here is an example of a ternary operation:
ex_num = 3

# [True value] if [Expression] else [False value]
color = 'blue' if ex_num < 5 else 'red'
print(color) # Output: blue



# Other notes
# -----------
'''
Instead of using `and` and `or` keywords, the `&` and `|` operators can perform similar functions
However, these operators are 'bitwise' operators and compare values via their bits to give an output
They aren't used as often and won't be discussed in this file to keep this repository for beginners.
'''
