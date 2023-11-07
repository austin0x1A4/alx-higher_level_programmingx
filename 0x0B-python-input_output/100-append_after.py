#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    new_lines = []

    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(new_lines
