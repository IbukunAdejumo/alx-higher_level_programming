#!/usr/bin/python3
"""Function to retrieve a list of lists
    of integers representing the pascal triangle
"""


def pascal_triangle(n):
    """Get list of lists of integers representing
        the pascal trinagle
    Args:
        n (int): [description]
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(2, n + 1):
        tmp = [0] + triangle[-1] + [0]
        triangle.append([sum(pair) for pair in zip(tmp, tmp[1:])])
    return triangle
