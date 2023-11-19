# Custom module for testing

test_string = 'Hello, world!'

def test_func(content):
  print(f'Printing: {content}')
  
class TestClass:
  def __init__(self, name):
    self.name = name
    self._value = 1
  
  def say_hello(self):
    print(f'Hello, {self.name}!')
