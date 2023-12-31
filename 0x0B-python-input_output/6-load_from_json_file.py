#!/usr/bin/python3                                                                                                                                                                        import json

def load_from_json_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return None
