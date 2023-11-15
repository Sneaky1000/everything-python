# Classes in practice

'''
Classes can be defined using the `class` keyword. Class names should always
be PascalCase (purely convention but should be followed).
'''

# Example of a video game monster class
class Monster:
  # Attributes (basically variables)
  health = 90
  energy = 40
  
  # Methods (basically functions scoped to the class)
  def attack(monster, damage): # IMPORTANT: Methods REQUIRE at least one parameter. Otherwise, the code will error out.
                               # Even if it's not "used," it's still required. This is because the first parameter of any
                               # method always references the object created by the class. This allows multiple objects
                               # to use separate instances of the same class's method.
    print('The monster has attacked!')
    print(f'{damage} was dealt.')
    # Attributes can be accessed directly inside the class itself
    # This is possible because of the first parameter referencing the object created by the class as mentioned above
    monster.energy -= 10
    print(f'The monster now has {monster.energy}/40 energy.')

# Creating an object with the class is simple (usually stored in a variable)
monster = Monster()

# Multiple objects can be created using the same class
monster2 = Monster()

# Attributes can be accessed via a `.` followed by the attribute name (same as when inside a class)
print(monster.health) # Output: 90

# Methods are accessed very similarly, but this time with an argument to pass to the parameter.
monster.attack(22)
'''
Output:

The monster has attacked!
22 was dealt.
The monster now has 30/40 energy.
'''

# Console/terminal separator for clarity
print('--------------------------------')

# Due to the properties of both attributes and methods mentioned above, `monster2` still has the base "stats"
# of the `Monster` class (health = 90, energy = 40, etc) - that's why the monster's energy won't be 20 when the
# attack method is called again (this time on a new object)
monster2.attack(35)
'''
Output:

The monster has attacked!
35 was dealt.
The monster now has 30/40 energy.
'''
