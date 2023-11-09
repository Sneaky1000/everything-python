# Loops

'''
While loops simply repeat code as long as a condtion is true/satisfied.

Loops, on the other hand, iterate over elements in a container.
'''

# Infinite while loop example (uncomment lines 8-11 to see it run)
'''
while True:
  print('INFINITE LOOP') # This will print forever because the condition is always met (CTRL + C to stop the loop in the terminal)
'''

# Finite while loop example
x = 1

while x < 11:
  print(x)
  x += 1
# Output: 1 \ 2 \ 3 \ 4 \ 5 \ 6 \ 7 \ 8 \ 9 \ 10 - where '\' means new line

# Breaking out of a loop can be done using the `break` keyword
y = 0

while y < 5:
  if y == 3:
    print('y = 3 so stop here')
    break

  print(y)
  y += 1
  
# Output: 0 \ 2 \ y = 3 so stop here

# To skip over an iteration of a loop, the `continue` keyword is used
z = 10
while z > 0:
  z -= 1

  if z < 6 and z > 1:
    continue

  print(z)
# Output: 9 \ 8 \ 7 \ 6 \ 1 \ 0

# Loops can be used to perform operations on each element of a container
basic_list = [1, 2, 3, 4, 5]
basic_tuple = (1, 2, 3, 4, 5)
basic_set = {1, 2, 3, 4, 5}
basic_dict = {1: 'one', 2: 'two', 3: 'three'}
basic_string = 'one two three'
basic_num = 3

nested_list = [[1, 2, 3], ['a', 'b', 'c'], [True, False, None]]

# Lists, tuples, sets, strings, and dictionaries are all iterable
for char in basic_string:
  print(char) # Output: o \ n \ e \   \ t \ w \ o \   \ t \ h \ r \ e \ e 

for key in basic_dict:
  print(key) # Output: 1 \ 2 \ 3

# The other containers work the same way as the list container

# Numbers are not iterable are require the `range()` function to make them iterable
for i in range(basic_num):
  print(i) # Output: 1 \ 2 \ 3

# `range()` is a very commonly used function and takes in three arguments, as shown below:
# range(start, end, step)
for i in range(0, basic_num, 2):
  print(i) # Output: 0 \ 2

# Nested lists, tuples, or sets can be iterated and so can their inner containers
# This can be done by nesting the for loops or by unpacking the outer container,
# then flattening (`chain()` from itertools) the iterables into one iterable object (This is more complex
# and won't be covered but it's good to keep in mind!).
for inner_list in nested_list:
  for value in inner_list:
    print(value) # Output: 1 \ 2 \ 3 \ a \ b \ c \ True \ False \ None


