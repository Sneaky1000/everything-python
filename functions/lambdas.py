# Lambda functions

'''
Lambda functions are single line functions that follow the following syntax:

`lambda param_x: expression`

The result is automatically returned
'''

# This lambda function is assinged to the global variable `a`
# It takes an argument for the parameter `x`, adds 1, then returns `x`
a = lambda x: x + 1
print(a(2)) # Output: 3

# This lambda function adds two numbers together and returns the result
add = lambda x, y: x + y
print(add(2, 3)) # Output: 5

# Other notes
# -----------
# 1. Lambda functions are popular for when a function takes another function as an argument
# 2. Lambda functions are also popular when dealing with graphical user interfaces
