#!/usr/bin/python3
"""
Contains function that writes a string to text file
"""


def write_file(filename='', text=''):
    """writes a string to text file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
