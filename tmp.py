import sys
import cv2
import numpy as np
from displayParameters import *

def displayImage(arguments):

    file = open(f"maze/{arguments[1]}","r")
    mazeData = []
    for x in file:
        x = x.rstrip("\n\r")
        x = x.split(" ")
        mazeData.append(x)
    file.close()
	
    m, n = len(mazeData), len(mazeData[0])
    adjustedBoxWidth = adjustWidth(m,n)
    if adjustedBoxWidth >= 0:
        pass
    else:
        return
    
    #print(f"height: {m}\nwidth: {n}")
    #print(adjustedBoxWidth)
    width = (adjustedBoxWidth * n) + (2*margin)
    height = (adjustedBoxWidth * m) + (2*margin)

    maze = np.zeros((height,width,3),np.uint8)

    # Margin
    #cv2.rectangle(maze,(margin,margin),((width-margin),(height-margin)),white,1)

    x, y = margin, margin#+border
    for row in mazeData:
        wall = -1
        top_floor = -1
        floor = -1
        top_floor = (top_floor+1)%2
        for i, value in enumerate(row):
            #x += border
            pt1 = (x,y)
            pt2 = ((x+adjustedBoxWidth),(y+adjustedBoxWidth))
            if value == '1':
                wall = (wall+1)%2
                img = cv2.imread(f"img/walls/{wall}.png")
                img = cv2.resize(img,(adjustedBoxWidth,adjustedBoxWidth))
                maze[y:(y+adjustedBoxWidth),x:(x+adjustedBoxWidth),:] = img
                #cv2.rectangle(maze,pt1,pt2,grey,-1)
            elif value == '0':
                floor = (floor+1)%2
                img = cv2.imread(f"img/floor/{top_floor}{floor}.png")
                img = cv2.resize(img,(adjustedBoxWidth,adjustedBoxWidth))
                maze[y:(y+adjustedBoxWidth),x:(x+adjustedBoxWidth),:] = img
                #cv2.rectangle(maze,pt1,pt2,black,-1)
            elif value == 'P':
                cv2.rectangle(maze,pt1,pt2,yellow,-1)
            elif value == 'S':
                img = cv2.imread("img/runner_color.png")
                img = cv2.resize(img,(adjustedBoxWidth,adjustedBoxWidth))
                ##############################
                #floor = (floor+1)%2
                #img2 = cv2.imread(f"img/floor/{top_floor}{floor}.png")
                #img2 = cv2.resize(img,(adjustedBoxWidth,adjustedBoxWidth))
                ##############################
                maze[y:(y+adjustedBoxWidth),x:(x+adjustedBoxWidth),:] = img
                #cv2.rectangle(maze,pt1,pt2,red,-1)
            elif value == 'D':
                img = cv2.imread("img/treasure.png")
                img = cv2.resize(img,(adjustedBoxWidth,adjustedBoxWidth))
                maze[y:(y+adjustedBoxWidth),x:(x+adjustedBoxWidth),:] = img
                #cv2.rectangle(maze,pt1,pt2,green,-1)
            x += adjustedBoxWidth
        x = margin
        y += (adjustedBoxWidth)#+border)

    # Display image
    if len(arguments) >= 3:
        cv2.imshow(f"MAZE SOLUTION USING {arguments[2]}",maze)
    else:
        cv2.imshow("MAZE",maze)
        
    cv2.waitKey(0)

def adjustWidth(m,n):
    if m <= 12 and n <= 23:
        adjustedBoxWidth = boxWidth
    elif m <= 14 and n <= 27:
        adjustedBoxWidth = 42
    elif m <= 16 and n <= 33:
        adjustedBoxWidth = 36
    elif m <= 21 and n <= 41:
        adjustedBoxWidth = 28
    elif m <= 28 and n <= 57:
        adjustedBoxWidth = 20
    elif m <= 35 and n <= 69:
        adjustedBoxWidth = 16
    elif m <= 45 and n <= 89:
        adjustedBoxWidth = 12
    elif m <= 53 and n <= 104:
        adjustedBoxWidth = 10
    elif m <= 63 and n <= 125:
        adjustedBoxWidth = 8
    elif m <= 79 and n <= 156:
        adjustedBoxWidth = 6
    else:
        print("\nWARNING!!! MAZE SIZE LIMIT EXCEEDED")
        return -1
    return adjustedBoxWidth

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\nWARNING!!! Please mention Maze File Name")
    else:
        displayImage(sys.argv)