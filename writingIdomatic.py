# /pythonPractice/writingIdomatic.py
# -*- coding: UTF-8 -*-

from __future__ import print_function
import operator as op

print("\n--Let's Practice!--\n")

# Notes:    When using 'if' statements do the error checking FIRST, then have the code that supposed to run normally, 
#           This lets a reader easily skip to what should happen.
# Ex: None


# Notes:    Chain arguments in the 'if' statements if you can
# Ex: None


# Notes:    Don’t repeat a '==' comparison in an 'if' statement, use a list or set when you can. ‘x’ in ‘some_list’ can return true or false
# Ex:

THOMAS = 'Thomas'
AMIR = 'Amir'
BRETT = 'Brett'
KIERAN = 'Kieran'
ANDREW = 'Andrew'

name = 'Thomas'

is_generic_name = False
if name == THOMAS or name == AMIR or name == BRETT:
    is_generic_name = True
print(is_generic_name) # prints 'True'

is_generic_name = False
is_generic_name = name in (THOMAS, AMIR, BRETT)
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

name_list = [ANDREW, THOMAS, AMIR, BRETT, KIERAN]
for name in name_list:
    for char in name:
        if char == 'x':
            print('Weird Name!')
    else: # matches the 'for' not the 'if'!
        print('All names are normal!')


# Notes:    Don't use a mutable object for method arguments. When the Python interpreter encounters a function definition, 
#           default arguments are evaluated to determine their value. This evaluation, however, occurs only once. 
#           Calling the function does not trigger another evaluation of the arguments.
# Ex:       

def func(a, b=[]):
    b.append(a)
    return b

print(func(10))
print(func(20))
print(func(30))


# Notes:    Return statements actually return the evaluation results of whatever expression you put in there.
# Ex:       

def all_equal(a, b, c):
    return a == b == c # This is the same as if( a == b == c ) and will return True/False


# Notes:    Use optional parameters to give methods more flexibility while at the time not burdening the user of the method
# Ex: None


# Notes:    Using *agrs and **kwargs as parameters allows us to have an arbitrary list of positional parameters
#           and/or keyword parameters. It also allows for backwards compatibility when adding additional method parameters.
# Ex: 

def for_console_output(func):
    def wrapper(*args, **kwargs):
        print('----------')
        print(str(func(*args, **kwargs)))
        print('----------')
    return wrapper

@for_console_output
def add(x, y):
    return x + y

add(3, 2)


# Notes:    Functions can be treated as variables and thus passed to other functions and returned as results from 
#           function calls. This is sometimes referred to as 'functional' programming. 
# Ex:

# This sequence of 4 methods can be replaced by one more generic method where you pass in an operator method 
def print_addition_table():
    for x in range(1,3):
        for y in range(1, 3):
            print(str(x + y) + '\n')

def print_subtraction_table():
    for x in range(1,3):
        for y in range(1, 3):
            print(str(x - y) + '\n')

def print_multiplication_table():
    for x in range(1,3):
        for y in range(1, 3):
            print(str(x / y) + '\n')

def print_division_table():
    for x in range(1,3):
        for y in range(1, 3):
            print(str(x / y) + '\n')

# As soon as you start repeating something, a computer can do it better
def print_table(operator):
    for x in range(1, 3):
        for y in range(1, 3):
            print(str(operator(x, y)) + '\n')

for operator in (op.add, op.sub, op.mul, op.div):
    print_table(operator)


# Notes:    Use 'print()' instead of 'print'. Python 3 is the future and we can't be stuck in the past
# Ex.       None


# Notes:    Exceptions are more wildly used in Python than in other languages. It can be a lot easier to write
#           EAFP (Easier to Ask For Forgiveness) code than LBYL (Look Before You Leap) code. EAFP code is also 
#           usually a lot easier to read than a lot of conditional statements.
# Ex.

# if, if, if
def get_log_level(config_dict)
    if 'ENABLE_LOGGING' in config_dict:
        if config_dict['ENABLE_LOGGING'] !=True:
            return None
        elif not 'LOG_LEVEL' in config_dict:
            return None
        else:
            return config_dict['LOG_LEVEL']
    else
        return None

# idiomatic

def get_log_level(config_dict)
    try:
        if config_dict['ENABLE_LOGGING']:
            return config_dict['LOG_LEVEL']
    except KeyError:
        return None # if either value wasn't present a 'KeyError' will be raised so return None