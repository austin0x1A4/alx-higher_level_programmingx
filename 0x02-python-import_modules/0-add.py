#!/usr/bin/python3
a = 1
b = 2
add_0 = __import__('add_0')
"imports the add function from add_0 file"
result = add_0.add(a, b)
print("{} + {} = {}".format(a, b, result))
