# Extra information on classes

'''
This file will go over the following:
  1. Private attributes
  2. `hasattr` and `setattr`
  3. doc string
'''

#--------------------#
# PRIVATE ATTRIBUTES #
#--------------------#

# Private attributes are attributes inside a class that cannot be influenced outside that class

# Here is the `Monster` class from previous files
class Monster:
  '''
  This class represents a simple monster enemy type

  Attributes - health, energy
  '''
  # Add attributes `health` and `energy`
  def __init__(self, health, energy):
    self.health = health
    self.energy = energy
    
    # Private attributes are technically impossible because Python always allows them to be changed
    # But Python developers have developed a convention that tells other devs an attribute should not be
    # changed - adding an underscore in front of an attribute means "don't change this attribute's value"
    self._id = 0
  
  # `attack` and `move` methods
  def attack(self, damage):
    print(f'The monster has attacked, dealing {damage} damage!')
    self.energy -= 20
  
  def move(self, speed):
    print(f'The monster has moved at a speed of {speed} units per second!')

#-------------------------#
# `hasattr` AND `setattr` #
#-------------------------#

# Start by creating an object using the `Monster` class
monster = Monster(100, 50)

# The `hasattr()` function is used to check if an attribute exists within a class
# Pass the object and attribute name as arguments
print(hasattr(monster, 'health')) # Output: True
print(hasattr(monster, 'stamina')) # Output: False

# The `setattr()` function is used to add an attribute to a class
# Pass the object, attribute name, and value of the attribute as arguments
setattr(monster, 'weapon', 'Sword')
print(monster.weapon) # Output: Sword

# Adding an attribute can also be done like this:
monster.shield_level = 3
print(monster.shield_level) # Output: 3

# Q: So, what's the point of `setattr()`?
# A: Adding multiple attributes in a for loop, for example, would be much more efficient with variables
#    for the attribute name that could be easily swapped rather than adding each attribute manually

#-------------#
# DOC STRINGS #
#-------------#

# The dunder method `__doc__` is used to help show documented information about an object
# It shows the string literal comments in an object
print(monster.__doc__)
'''
Output:

  This class represents a simple monster enemy type

  Attributes - health, energ
'''

# The `help()` function also shows information about an object but doesn't require string literals
help(monster)
'''
Ouput:

class Monster(builtins.object)
 |  Monster(health, energy)
 |  
 |  This class represents a simple monster enemy type
 |  
 |  Attributes - health, energy
 |  
 |  Methods defined here:
 |  
 |  __init__(self, health, energy)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  attack(self, damage)
 |      # `attack` and `move` methods
 |  
 |  move(self, speed)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
'''

# This is extremely helpful when dealing with an object there is no knowledge on.
# A lot can be passed into the `help()` function to get information about that thing
# help(str) # This will print all documentation on strings in Python

# Note: Only one instance of `help()` can be used at a time
#       To see `help(str)`, comment out the other `help()` functions
