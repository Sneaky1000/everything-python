# Variables

# Variable assignment is handled with the '=' operator
result = 5 + 10
print(result) # Output: 15

# Variables can be used just like other programming languages
result2 = result / 2
print(result2) # Output: 7.5

# Local v3ariables in Python should use snake_case, not camelCase syntax
variable_name = 0

# Variables have the same features as other languages when it comes to operations
num1 = 1
num1 += 2
print(num1) # Output: 3

num2 = 1
num2 -= 2
print(num2) # Output: -1

num3 = 1
num3 *= 2
print(num3) # Output: 2

num4 = 1
num4 /= 2
print(num4) # Output: 0.5

# Variables assinged solely with the '=' operator are scoped to the function/region they're created in
num5 = 1 # This can be used globally since it isn't defined in a function

# Variables can be used globally when defined in a function by using the 'global' keyword
# Global variables should be all uppercase and snake_case
global NUM_SIX # Declare the variable (global variables cannot be initialized by adding the '=' operator on the same line without a semi-colon
global NUM7; NUM7 = 1 # This works
global NUM_8
NUM_8 = 1 # This also works


# Other notes
# -----------
# 1. Variable names cannot start with a number
# 2. Variable names cannot contain special characters (e.g. @, !, ^, %, $, etc.)

