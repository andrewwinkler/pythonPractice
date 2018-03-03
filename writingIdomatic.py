# /pythonPractice/writingIdomatic.py
# -*- coding: UTF-8 -*-

from __future__ import print_function

print("\n--Let's Practice!--\n")

# Notes:    When using 'if' statements do the error checking FIRST, then have the code that supposed to run normally, 
#           This lets a reader easily skip to what should happen.


# Notes:    Chain arguments in the 'if' statements if you can


# Notes:    Don’t repeat a '==' comparison in an 'if' statement, use a list or set when you can. ‘x’ in ‘some_list’ can return true or false
# Ex:

is_generic_name = False
name = 'Tom'
if name == 'Tom' or name == 'Dick' or name == 'Harry':
    is_generic_name = True
print(is_generic_name) # prints 'True'

name = 'Tom'
is_generic_name = name in ('Tom', 'Dick', 'Harry')
print(is_generic_name) # also prints 'True'


# Notes:    Use the implicit 'True' from objects instead of 'if X == True'
#           Same for 'False', if a list is empty 'if my_list' will evaluate to false
#           'is not None' is important too as it will still hold true for '0' (if you are evaluating an index for example)


# Notes:    Use 'if' and 'else' as short ternary operators
# Ex:

foo = True
value = 10
if foo:
    value = 20
print(value) # prints 20

foo = True
value = 20 if foo else 10
print(value) # also prints 20 but much cleaner evaluation


# Notes:    Use 'enumarate' intead of creating an index variable