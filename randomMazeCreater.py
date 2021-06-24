'''
    Run this program to create random maze.
    Then, add source/start & end/destination points in the created maze.
'''

import random

file = open("maze/maze_rand.txt","w")
for row in range(25):
    a = ""
    for col in range(45):
        if col < 44:
            a = a+f"{random.randint(0,1)} "
        else:
            a = a+f"{random.randint(0,1)}\n"
    file.write(a)
file.close()