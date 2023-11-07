#!/usr/bin/python3

from pascal_triangle import pascal_triangle

def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join(map(str, row)))

print_triangle(pascal_triangle(5))
