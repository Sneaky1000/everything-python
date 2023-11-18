# Classes and scope

'''
Because every method has a reference to the class, it's easy to get and change
class attributes. This means that methods are generally easier to work with
as they rely much less on parameters, the 'global' keyword, and return values
(although these are still usable). Objects can even be influenced from outside
and from a local scope function.
'''

# Scope demonstration with the `Monster` class and an `updateHP()` function
def updateHP(amount):
  monster.health += amount

class Monster:
  # Add attributes `health` and `energy`
  def __init__(self, health, energy):
    self.health = health
    self.energy = energy

# Create `monster` object using the `Monster` class (100 health. 50 energy)
monster = Monster(100, 50)

# Despite the updateHP() function using the `monster` object seemingly before being initialized,
# it will still work because of the `Monster` class...
updateHP(20)
print(monster.health) # Output: 120

'''
Important: If `monster.health` was replaced with a variable called `health` and the `Monster` class
was removed, calling `updateHP()` will error out because the variable was assigned after the function
was created. This can be fixed using the `global` keyword (to make the variable a global variable) but
becomes messy.

It is also important to know that, most of the time, these functions will simply be set as methods in the
class due to the efficiency and cleanliness of the code when written this way.
'''
