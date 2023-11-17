# __dunder__ methods (Double-underscore methods)

'''
A dunder method is a method that is not called by the user. Instead, it is called
when something happens. For example, `__init__` is called when an object is created.
`__len__` is called when an object is passed into `len()` built-in function. `__abs__`
is called when an object is passed into `abs()` built-in function
'''

# Let's look at a previous class created in 'classes_in_practice.py'
class Monster:
  # Because the attributes are being assigned in the `__init__` method, there is no need for
  # these attributes to be initialized here

  # health = 90
  # energy = 40
  
  # Remember that __init__ is called when an object is created...
  # Again, the first parameter is the reference to the object created
  # Here, the 'health' and 'energy' attributes can be changed from the defaults (90, 40 respectively)
  def __init__(self, health = 90, energy = 40): # This method will run automatically when an object using this class is created
    print('The monster has been created')
    
    # The 'self' parameter makes the health and energy attributes being assigned here go to the OBJECT instead of the class
    # This allows the health and energy to be different for each object created using this class if desired.
    self.health = health
    self.energy = energy
    
  # Q: What if a length of this class is needed?
  # A: Use the `__len__` method to assign a length to the class
  def __len__(self):
    return self.health

  # Q: What if the absolute value of this class is needed?
  # A: Use the `__abs__` method to get the absolute value
  def __abs__(self):
    # Setting this to a negative value will return the negative value
    # The "absolute" value depends on what the user has assigned that value to be
    return self.energy

  def attack(self, damage):
    print('The monster has attacked!')
    print(f'{damage} was dealt.')
    self.energy -= 10
    print(f'The monster now has {self.energy} energy.')
    
  def move(self, speed):
    print('The monster has moved')
    print(f'It has a speed of {speed}')


# When this object is created with the 'Monster' class, it will run `__init__`
monster1 = Monster() # Output: The monster has been created
print(monster1.health) # Output: 90

# Example of alternative 'health' and 'energy' attributes using `__init__`
# The name of the parameter included in the argument assignment is optional
monster2 = Monster(10, energy = 12) # '10' is the health value
# Output: The monster has been created
print(monster2.health) # Output: 10
print(monster2.energy) # Output: 12

# Get the length of the monster (in this case, 'health')
print(len(monster2)) # Output: 10

# Get the absolute value of the monster (in this case, 'energy')
# If the energy value is set to a negative value, it will still be negative, unfortunately
# The "absolute" value is just the value that was set to be "absolute" by the user
print(abs(monster2)) # Output: 12

# The `dir()` built-in function will show all the dunder mehthods that can be used on an object
# It also lists all the attributes and methods created in the class by the user
# The "dir" part stands for "directory" or "directory listings"
print(dir(monster1))
'''
Output (all one line):

['__abs__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
'__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
'__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__',
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
'__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attack', 'energy',
'health', 'move']
'''

# `__dict__` can be used to show the attributes of an object
# The `vars()` built-in function does the same thing for objects
print(monster2.__dict__) # Output: {'health': 10, 'energy': 12}
print(vars(monster2)) #  Output: {'health': 10, 'energy': 12}

# Classes can also be turned into functions via the `__call__` method
class Fish:
  def __call__(self):
    return 'The fish was called'
  
  # `__add__` adds two numbers together
  def __add__(self, other):
    return 10 + other

# Calling the Fish class after creating an object with it
fish1 = Fish()

# Add '()' to call it just like any other function
print(fish1()) # Output: The fish was called

# Printing the `__add__` dunder method
print(fish1 + 10) # Output: 20

# Other notes:
# ------------
# 1. Do some research and see what other dunder methods do! There are several that are very useful.
