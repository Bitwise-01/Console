# Console 
A simple console app

### Usage
1) Console class must be inherited into your main class
2) All methods that can be invoked by the user must start with a cmd_
3) All methods that can be invoked by the user must take *args as an argument
4) All methods that can be invoked by the user have their arguments stored in args[0]

### Example
```python
from console import Console 

class Calculator(Console):

 def __init__(self):
  try:super().__init__()
  except TypeError:super(Calculator, self).__init__()

 def display(func):
  def wrapper(*args):
   answer = func(*args)
   print('\nAnswer: {}\n'.format(answer))

  wrapper.__doc__ = func.__doc__
  return wrapper

 def extract_nums(self, nlist):
  return [int(_) for _ in nlist if _.isdigit()]

 @display
 def cmd_add(self, *args):
  '''Description: add numbers\nUsage: add 1 2 3'''

  if not len(args):return
  inputs = args[0]
  numbers = self.extract_nums(inputs)
  total = numbers[0]

  for _ in range(1, len(numbers)):
   total += numbers[_]
  return total
 
 @display
 def cmd_sub(self, *args):
  '''Description: subtract numbers\nUsage: sub 5 3 1'''

  if not len(args):return
  inputs = args[0]
  numbers = self.extract_nums(inputs)
  total = numbers[0]

  for _ in range(1, len(numbers)):
   total -= numbers[_]
  return total

if __name__ == '__main__':
 my_app = Calculator()
 my_app.start_loop()
```