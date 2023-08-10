#!/usr/bin/python3

for char in range(122, 96, -1):
    print("{:c}".format(char), end="")
    char -= 32
    print("{:c}".format(char), end="")
