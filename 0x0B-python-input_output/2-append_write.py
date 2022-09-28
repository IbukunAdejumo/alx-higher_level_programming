#!/usr/bin/python3
"""
Module 4-append_write
Contains function that appends to text file
"""


def append_write(filename="", text=""):
    """appends to text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return(f.write(text))
