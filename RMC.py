'''
    Run this program to create random maze.
    Then, add source/start & end/destination points in the created maze.
'''

import random

def getMaze(width, height):
    maze = []
    for row in range(height):
        a = []
        for col in range(width):
            a.append(random.randint(0,1))
        maze.append(a)
    return maze