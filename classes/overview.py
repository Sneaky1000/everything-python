# Classes overview

'''
It's important to understand what an object is before getting into classes. An object
is a container for variables and functions. The best way to understand this is actually
through video games. For example, a monster object might contain:

variables for: health, mana, stamina, damage, etc
functions for: attack, movement, animations, etc

In objects, variables are called 'attributes' and functions are called 'methods'.

Back to the video game example... it's possible to have multiple monster objects that
all have different attribute values (one might have more health or a different animation
than another). This is because the attributes and methods are locally scoped to the object.

Objects can also interact with each other. If one monster attacked another, the attribute
'health' of the attacked monster could be lowered through some function. This leads to the
topic of 'object-oriented programming (OOP)'. This is basically when code is organized via
objects.

So, what are classes then?

A class is the blueprint for an object. When creating an object, a class is needed first.
A class also accepts arguments to customize the object. One class can inherit from another
class, with the resulting objects having attributes and methods from both classes.

Why classes and objects?

1. They organize complex code.
2. They help create re-usable code.
3. They are used everywhere!
4. Some modules REQUIRE classes to be made.
5. They make it easier to work with scope.
'''
