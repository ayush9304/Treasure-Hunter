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
    
    width = (adjustedBoxWidth * n) + (2*margin)
    height = (adjustedBoxWidth * m) + (2*margin)

    maze = np.zeros((height,width,3),np.uint8)

    # Margin
    maze = drawBoundary(width,height,maze,margin)

    x, y = margin, margin
    for row in mazeData:
        wall = -1
        top_floor = -1
        floor = -1
        top_floor = (top_floor+1)%2
        for i, value in enumerate(row):
            pt1 = (x,y)
            pt2 = ((x+adjustedBoxWidth),(y+adjustedBoxWidth))
            if value == '1':
                wall = (wall+1)%2
                img = cv2.imread(f"img/walls/{wall}.png")
                img = cv2.resize(img,(adjustedBoxWidth,adjustedBoxWidth))
                maze[y:(y+adjustedBoxWidth),x:(x+adjustedBoxWidth),:] = img
            elif value == '0':
                floor = (floor+1)%2
                img = cv2.imread(f"img/floor/{top_floor}{floor}.png")
                img = cv2.resize(img,(adjustedBoxWidth,adjustedBoxWidth))
                maze[y:(y+adjustedBoxWidth),x:(x+adjustedBoxWidth),:] = img
            elif value == 'P':
                cv2.rectangle(maze,pt1,pt2,yellow,-1)
            elif value == 'S':
                s_img = cv2.imread("img/loki3_transparent.png")
                s_img = cv2.resize(s_img,(adjustedBoxWidth,adjustedBoxWidth))
                floor = (floor+1)%2
                l_img = cv2.imread(f"img/floor/{top_floor}{floor}.png")
                l_img = cv2.resize(l_img,(adjustedBoxWidth,adjustedBoxWidth))
                
                img = addObject(l_img,s_img,10)

                maze[y:(y+adjustedBoxWidth),x:(x+adjustedBoxWidth),:] = img
            elif value == 'D':


                s_img = cv2.imread("img/tessract.png")
                s_img = cv2.resize(s_img,(adjustedBoxWidth,adjustedBoxWidth))
                floor = (floor+1)%2
                l_img = cv2.imread(f"img/floor/{top_floor}{floor}.png")
                l_img = cv2.resize(l_img,(adjustedBoxWidth,adjustedBoxWidth))

                img = addObject(l_img,s_img,25)

                maze[y:(y+adjustedBoxWidth),x:(x+adjustedBoxWidth),:] = img
            x += adjustedBoxWidth
        x = margin
        y += (adjustedBoxWidth)

    # Display image
    if len(arguments) >= 3:
        cv2.imshow(f"MAZE SOLUTION USING {arguments[2]}",maze)
    else:
        cv2.imshow("TREASURE HUNTER",maze)
        
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


def drawBoundary(width,height,maze,boundary):
    left = cv2.imread("img/boundary/0.png")
    length = (left.shape[0]//left.shape[1])*10
    left = cv2.resize(left,(boundary,length))
    top = cv2.rotate(left,cv2.ROTATE_90_CLOCKWISE)
    bottom = cv2.rotate(left,cv2.ROTATE_90_COUNTERCLOCKWISE)
    right = cv2.rotate(left,cv2.ROTATE_180)

    # Drawing left & right boundary
    n = (height//length)+1
    overflowy = int(((height/length)-(height//length))*length)
    y=0
    for i in range(n):
        if i == n-1:
            maze[y:(y+overflowy),0:boundary,:] = left[0:overflowy,0:boundary,:]
            maze[y:(y+overflowy),(width-boundary):width,:] = right[0:overflowy,0:boundary,:]
        else:
            maze[y:(y+length),0:boundary,:] = left
            maze[y:(y+length),(width-boundary):width,:] = right
        y = y+length

    # Drawing top & bottom boundary
    offset = boundary*.8
    n = ((width-(2*offset))//length)+1
    overflowx = int((((width-(2*offset))/length)-((width-(2*offset))//length))*length)
    x=int(offset)
    for i in range(int(n)):
        if i == n-1:
            maze[0:boundary,x:(x+overflowx),:] = top[0:boundary,0:overflowx,:]
            maze[(height-boundary):height,x:(x+overflowx),:] = bottom[0:boundary,0:overflowx,:]
        else:
            maze[0:boundary,x:(x+length),:] = top
            maze[(height-boundary):height,x:(x+length),:] = bottom
        x = x+length
    return maze


def addObject(background,logo,threshold):
    height, width, channels = logo.shape
    roi = background[0:height,0:width]

    logoGray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(logoGray,threshold,255,cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
    fg = cv2.bitwise_and(logo,logo,mask=mask)

    img = cv2.add(bg,fg)
    background[0:height,0:width] = img
    return background

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\nWARNING!!! Please mention Maze File Name")
    else:
        displayImage(sys.argv)