# /pythonPractice/writingIdomatic.py
# -*- coding: UTF-8 -*-

from __future__ import print_function
import operator as op
import requests
from collections import namedtuple

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
def get_log_level(config_dict):
    if 'ENABLE_LOGGING' in config_dict:
        if config_dict['ENABLE_LOGGING'] !=True:
            return None
        elif not 'LOG_LEVEL' in config_dict:
            return None
        else:
            return config_dict['LOG_LEVEL']
    else:
        return None

# idiomatic
def get_log_level(config_dict):
    try:
        if config_dict['ENABLE_LOGGING']:
            return config_dict['LOG_LEVEL']
    except KeyError:
        return None # if either value wasn't present a 'KeyError' will be raised so return None


# Notes:    Avoid swallowing useful exceptions with bare except clauses. Specifying an exception is important
#           for debugging and tracing back the error. If you need to know when an exception occurs but don't
#           want to deal with it then use a bare 'raise' at the end of your 'except' block to re-raise the 
#           exception. This way the the code runs and the user still gets useful information if something goes wrong. 
# Ex.

# Harmful
def get_json_response(url):
    try:
        result = requests.get(url)
        return result.json()
    except:
        print('Oopsies, something went wrong')
        return None

# Idiomatic
def get_json_response(url):
    try:
        result = requests.get(url)
        return result.json()
    except:
        # Do whatever you want, but don't handle the exception
        raise


# Notes:    The simply put rule of thumb for rasing exceptions is: never raise a core Python exception in your own code.
#           If something goes wrong you and the user won't know if was from your code or any other numerous parts of
#           the code or built in libraries that raise the exact same exception. 


# Notes:    No need to use a temporary variable when swapping values
#
# Ex.

# Harmful
foo = 'Foo'
bar = 'Bar'
temp = foo
foo = bar
bar = temp

# Idiomatic
foo = 'Foo'
bar = 'Bar'
(foo, bar) = (bar, foo)


# Notes:    Use the 'ord' function to get the ASCII value
#
# Ex.

some_string = 'Andrew'
for c in some_string:
    print(ord(c))


# Notes:    Use .format for string formatting
#
# Ex:

# Harmful
def get_formatted_user_info(user):
    return 'Name: %s, Age: %s, Sex: %s' % (user.name, user.age, user.sex)

# Idiomatic 
def get_formatted_user_info(user):
    return 'Name: {user.name}, Age: {user.age}, Sex: {user.sex}'.format(user=user)


# Notes:    Use list comprehension (generator expression) whenever you can. Use the build in 'sum' function.
#           Use 'all' to determine of all elements of an iterable are true.


# Notes:    Use 'xrange(10000)' insted of 'range(10000)' so that the range list is not stored in memory


# Notes:    Use dictionaries as switch statements
# Ex: 

def apply_operation(left_operand, right_operand, operator):
    import operator as op
    operator_mapper = {
        '+': op.add, 
        '-': op.sub, 
        '*': op.mul, 
        '/': op.truediv
        }
    return operator_mapper[operator](left_operand, right_operand)


# Notes:    The dictionary 'get' method has a default parameter to return if the key is does not exist:
#           
#           dict.get(key, default = None)
#           key − This is the Key to be searched in the dictionary.
#           default − This is the Value to be returned in case key does not exist.


# Notes:    Can use dictionary comprehension similarly to list comprehension
#
#           user_email = {user.name: user.email for user in users_list if user.email}


# Notes:    When comparting data and intersecting data use sets
#
# Ex:

# Harmful
def get_both_popular_and_active_users():
    # Assume the following two functions each return a list of user names
    most_popular_users = get_list_of_most_popular_users()
    most_active_users = get_list_of_most_active_users()
    popular_and_active_users = []
    for user in most_active_users:
        if user in most_popular_users:
            popular_and_active_users.append(user)
    return popular_and_active_users

# Idiomatic
def get_both_popular_and_active_users():
    # Assume the following two functions each return a list of user names
    return(set(get_list_of_most_active_users()) & set(get_list_of_most_popular_users()))

list_one = ['Manny', 'Moe', 'Jack']
list_two = ['Larry', 'Moe', 'Curly']

# Harmful
def has_duplicate_harmful(list_one, list_two):
    duplicate_name = False
    for name in list_one:
        if name in list_two:
            duplicate_name = True
    return duplicate_name

# Idiomatic
def has_duplicate_idiomatic(list_one, list_two):
    return set(list_one) & set(list_two)

if has_duplicate_harmful:
    print('Duplicate')
if has_duplicate_idiomatic:
    print('Duplicate')

# You can even use sets to just remove duplicate data from a list
employee_surnames = list()
unique_surnames = set(employee_surnames)


# Notes:    Use named tuple to access fields by name instead of index
#
# Ex:
Employee = namedtuple('Employee',['first_name', 'last_name', 'department', 'manager'])


# Notes:    Use '_' for unconsumed data and variables


# Notes:    Unpack data all at once using tuples and at the same time use tuples to return
#           more than one value


# Notes:    Don't overuse calasses just to encapsulate methods, it's okay to create methods
#           on their own that are importable

# Notes:    Use 'isinstance()' when evaluting the type of an object


# Notes:    Use a single underscore for 'private methods', they will not be imported if __all__
#           is used. Use two underscores for 'private' variables, it will invoke name mangling 
#           which changes the name to _classname__attributename when called 


# Notes:    Use 'setters' and 'getters' like everyone else
#
# Ex:

class Product(object):

    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        # now if we need to change how price is calculated, we can do it
        # here (or in the "setter" and __init__)
        return self._price * TAX_RATE

    @price.setter
    def price(self, value):
        # The "setter" function must have the same name as the property
        self._price = value


# Notes:    Use __str__ for a human readable representation of your class and use __repr__
#           for a machine readable representation of your class


# Notes:    USe a context manager to ensure resources are properly managed
#
# Ex:

# Harmful
# file_handle = open(path_to_file, 'r')
#     for line in file_handle.readlines():
#         # Something

# Idiomatic
# with open(path_to_file, 'r') as file_handle:
#         for line in file_handle:
#             # Something


# Notes:    Use generators instead of list comprehension for expensive or 'infinite' sequences.
#           The main difference being that a list comprehension generates a list object and fills 
#           in all of the elements immediately. For large lists, this can be prohibitively expensive. 
#           The generator returned by a generator expression, on the other hand, generates each element 
#           “on-demand”
#
# Ex:

def get_twitter_stream_for_keyword(keyword):
    """
    Now, 'get_twitter_stream_for_keyword' is a generator
    and will continue to generate Iterable pieces of data
    one at a time until 'can_get_stream_data(user)' is
    False (which may be never).
    """

    imaginary_twitter_api = ImaginaryTwitterAPI()
    while imaginary_twitter_api.can_get_stream_data(keyword):
        yield imaginary_twitter_api.get_stream(keyword)


# Notes:    Use absolute imports instead of relative and don't use a '*' in your imports.
#           Also use try/catch blocks to check if a package is available for import


# Notes:    Use __init__.py to set what is available for import

# Notes:    Use __main__.py to invoke packages as scripts. This file is only invoked when 
#           the -m flag is passed to the interpreter (in which case <package>.__main__ is executed 
#           as the main module) or when a directory or zipfile is passed as an argument to the interpreter


# Notes:    Call sys.exit(main()) under __name__ == '__main__' and write everyone else in main() itself
