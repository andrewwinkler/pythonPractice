# /pythonPractice/writingIdomatic.py

from __future__ import print_function

print("\n--Let's Practice!\n--")

# Notes:    When using if statements do the error checking FIRST, then have the code that supposed to run normally, 
#           This lets a reader easily skip to what should happen.

# Notes:    Chain arguments in the if statements if can

# Notes:    Don’t repeat a '==' comparison in an if statement, use a list or set when you can. ‘x’ in ‘some_list’ can return true or false
# Ex:

name = 'Tom'
is_generic_name = name in ('Tom', 'Dick', 'Harry')
print(is_generic_name) # prints 'True'