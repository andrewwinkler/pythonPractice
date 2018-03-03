# /pythonPractice/writingIdomatic.py
# -*- coding: UTF-8 -*-

from __future__ import print_function

print("\n--Let's Practice!--\n")

# Notes:    When using 'if' statements do the error checking FIRST, then have the code that supposed to run normally, 
#           This lets a reader easily skip to what should happen.
# Ex: None


# Notes:    Chain arguments in the 'if' statements if you can
# Ex: None


# Notes:    Don’t repeat a '==' comparison in an 'if' statement, use a list or set when you can. ‘x’ in ‘some_list’ can return true or false
# Ex:

is_generic_name = False
name = 'Thomas'
if name == 'Thomas' or name == 'Amir' or name == 'Brett':
    is_generic_name = True
print(is_generic_name) # prints 'True'

name = 'Thomas'
is_generic_name = name in ('Thomas', 'Amir', 'Brett')
print(is_generic_name) # also prints 'True'


# Notes:    Use the implicit 'True' from objects instead of 'if X == True'
#           Same for 'False', if a list is empty 'if my_list' will evaluate to false
#           'is not None' is important too as it will still hold true for '0' (if you are evaluating an index for example)
# Ex: None


# Notes:    Use 'if' and 'else' as short ternary operators
# Ex:

some_bool = True
value = 10
if some_bool:
    value = 20
print(value) # prints 20

some_bool = True
value = 20 if some_bool else 10
print(value) # also prints 20 but much cleaner evaluation


# Notes:    Use 'enumerate' instead of creating an index variable (just like the use in 'for' loops)
# Ex: None


# Notes:    Use the 'in' keyword to iterate over an iterable (just like all 'for' loops)
# Ex: None


# Notes:    For loops can have an 'else' clause that is executed if the iterator is exhausted.
#           It is not executed if the loop is ended prematurely
# Ex:

name_list = ['Andrew', 'Thomas', 'Amir', 'Brett', 'Kieran']
for name in name_list:
    for char in name:
        if char == 'x':
            print('Weird Name!')
    else: # matches the 'for' not the 'if'!
        print('All names are normal!')
        