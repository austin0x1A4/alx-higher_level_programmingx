#!/usr/bin/python3

def is_same_class(obj, a_class):
    """Returns True if obj is an instance of the specified class, otherwise False."""
    return type(obj) is a_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))
