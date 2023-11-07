#!/usr/bin/python3
import sys
import os
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# Check if the JSON file exists, and if not, create an empty list
filename = 'add_item.json'
my_list = []

if os.path.isfile(filename):
    my_list = load_from_json_file(filename)

# Add the command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(my_list, filename)
