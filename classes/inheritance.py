# Simple and complex inheritance

'''
Inheritance means that one class gets attributes and methods from another class (or classes).
A class can inherit from an unlinmited number of other classes and vice versa. Inheritance
can get very complex. However, most of the time, simple inheritance is all that's required.
'''

# -------------------#
# SIMPLE INHERITANCE #
# -------------------#

# This will be a demonstration of simple inheritance using the `Monster` class as the parent
class Monster:
  # Add attributes `health` and `energy`
  def __init__(self, health, energy):
    self.health = health
    self.energy = energy
  
  # `attack` and `move` methods
  def attack(self, damage):
    print(f'The monster has attacked, dealing {damage} damage!')
    self.energy -= 20
  
  def move(self, speed):
    print(f'The monster has moved at a speed of {speed} units per second!')

# Now, the child class `shark` can inherit from the `Monster` class using parentheses
# almost like passing it as an argument, but now, the parent class is being passed
# for the child class to take attributes/methods from
class Shark(Monster):
  # Set `speed` attribute and get desired attributes from the parent class (`Monster`)
  def __init__(self, speed, health, energy):
    self.speed = speed
    # Get desired attributes from the parent class using the __init__ method on the `Monster` class
    # `self` now refers to the `Shark` class, not the `Monster` class...
    # However this is outdated (it still works)
    # Monster.__init__(self, health, energy)
    
    # Instead the new method is to call the `super()` function like this...
    super().__init__(health, energy) # No need for `self` anymore!

  # Add new `bite()` method
  def bite(self):
    print('Shark uses BITE')

  # Methods/attributes can be overridden by child classes by re-defining them
  def move(self):
    print(f'The shark has swam at a speed of {self.speed} units per second')

# Create a `shark` object using the `Shark` class
# Set speed to 120, health to 100, and energy to 50
shark = Shark(120, 100, 50)

# Calling a child class (`Shark`) method
shark.move() # Output: The shark has swam at a speed of 120 units per second

# Calling a parent class (`Monster`) method
shark.attack(10) # Output: The monster has attacked, dealing 10 damage!

# Getting a child class attribute
print(shark.speed) # Output: 120

# Getting a parent class attribute that has been inherited
print(shark.health) # Output: 100

# Simple inheritance is extremely important and needs to be understood before moving on to...

#---------------------# 
# COMPLEX INHERITANCE #
#---------------------#

# This complex inheritance example will use a re-named `Monster` class
class Mob:
  # Add attributes `health` and `energy`
  def __init__(self, health, energy, **kwargs): # `**kwargs` stores any other arguments in a separate dictionary (it unpacks the arguments)
    print(kwargs) # Output: {'speed': 120, 'has_scales': False}
    self.health = health
    self.energy = energy
    # The line below will be explained in the `Whale` class
    # kwargs will now take `speed` and `has_scales` from the `Fish` class (and more if added!)
    super().__init__(**kwargs)
  
  # `attack` and `move` methods
  def attack(self, damage):
    print(f'The monster has attacked, dealing {damage} damage!')
    self.energy -= 20
  
  def move(self, speed):
    print(f'The monster has moved at a speed of {speed} units per second!')

# Define a class for any fish/sea creatures
class Fish:
  # Add `speed` and `has_scales` attributes
  def __init__(self, speed, has_scales):
    self.speed = speed
    self.has_scales = has_scales

  # `swim` method
  def swim(self):
    print(f'The fish is swimming at a speed of {self.speed}')

# `Whale` class that inherits from the `Mob` and `Fish` classes
# Order matters! Method Resolution Order (MRO) is the order
# that Python sees classes in
class Whale(Mob, Fish):
  # Add `bite_strength` attribute and inherit attributes from parent classes
  def __init__(self, bite_strength, health, energy, speed, has_scales):
    self.bite_strength = bite_strength
    # To inherit from parent classes use the `super()` function as before
    # This time, it's important to understand the MRO of the class...
    # In this case, `Whale` is index '0', `Mob` is index '1', and `Fish` is index '2' 
    # So this super() function calls the first item of inheritance, `Mob`
    # super().__init__(health, energy)
    # But this wouldn't get the other attributes from the `Fish` class
    # This is where keyword arguments come into play (kwargs)
    # Here, all attributes need to be assigned to their respective arguments
    super().__init__(health = health, energy = energy, speed = speed, has_scales = has_scales)
    
  
# Creating an object with the `Whale` class
whale = Whale(
  50, # Bite strength
  200, # Health
  55, # Energy
  120, # Speed
  False # Has scales?
)

print(whale.speed) # Output: 120
whale.attack(12) # Output: The monster has attacked, dealing 12 damage!
whale.swim() # Output: The fish is swimming at a speed of 120

