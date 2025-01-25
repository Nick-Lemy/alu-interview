#!/usr/bin/python3
"""
    Method that calculate the fewest number of operations.
"""

def rain(walls):
    """
    Interestin module
    """
    if len(walls) == 0:
        return 0
    else:
        if walls[0] == 0:
            walls.pop(0)
        elif walls[-1] == 0:
            walls.pop(-1)
        return (len(walls) - 1)*2

