import sys
import cv2
import numpy as np
from displayParameters import *

def generateImage(mazeData, path_list=None):
	
    m, n = len(mazeData), len(mazeData[0])

    adjustedBoxWidth = adjustBoxWidth(n, m)

    width = (adjustedBoxWidth * n) + (2*margin)
    height = (adjustedBoxWidth * m) + (2*margin)

    maze = np.zeros((height,width,3),np.uint8)
    pathFrame = []

    # Margin
    maze = drawBoundary(width,height,maze)

    # Source Box data
    s_x = None
    s_y = None
    s_floor = None
    s_loki = None

    to_animate = False
    x, y = margin, margin
    for row in mazeData:
        wall = -1
        top_floor = -1
        floor = -1
        top_floor = (top_floor+1)%2
        for value in row:
            if value == 1:
                wall = (wall+1)%2
                img = cv2.imread(f"img/walls/{wall}.png")
                img = cv2.resize(img,(adjustedBoxWidth,adjustedBoxWidth))
                maze[y:(y+adjustedBoxWidth),x:(x+adjustedBoxWidth),:] = img
            
            elif value == 0 or value == 'P' or value == 'p':
                floor = (floor+1)%2
                img = cv2.imread(f"img/floor/{top_floor}{floor}.png")
                img = cv2.resize(img,(adjustedBoxWidth,adjustedBoxWidth))
                maze[y:(y+adjustedBoxWidth),x:(x+adjustedBoxWidth),:] = img
                if value == 'P' or value == 'p':
                    to_animate = True
                    pathFrame.append(((int(x+(adjustedBoxWidth/2))),(int(y+(adjustedBoxWidth/2)))))

            elif value == 'S' or value == 's':
                s_img = cv2.imread("img/loki3_transparent_resized.png")
                s_img = cv2.resize(s_img,(adjustedBoxWidth,adjustedBoxWidth))
                floor = (floor+1)%2
                l_img = cv2.imread(f"img/floor/{top_floor}{floor}.png")
                l_img = cv2.resize(l_img,(adjustedBoxWidth,adjustedBoxWidth))

                #For animation purpose (maze without loki image)---v
                s_x = x
                s_y = y
                s_floor = l_img.copy()
                s_loki = s_img.copy()
                #--------------------------------------------------^

                img = addObject(l_img,s_img,10)
                maze[y:(y+adjustedBoxWidth),x:(x+adjustedBoxWidth),:] = img
            
            elif value == 'D' or value == 'd':
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

    maze2 = maze.copy()
    if s_x is not None and  s_y is not None:
        maze2[s_y:(s_y+adjustedBoxWidth),s_x:(s_x+adjustedBoxWidth),:] = s_floor

    ####################################################################################
    if to_animate:
        animate(maze2, s_loki, path_list, steps, adjustedBoxWidth)
    ####################################################################################

    else:
        return maze, maze2, s_loki, adjustedBoxWidth
        


def adjustBoxWidth(width, height):
    if width >= 95 or height >= 67:
        return int(boxWidth/2.2)
    elif width >= 67 or height >= 50:
        return int(boxWidth/1.85)
    elif width >= 50 or height >= 39:
        return int(boxWidth/1.6666)
    else:
        return boxWidth

def drawBoundary(width,height,maze):
    left = cv2.imread("img/boundary/0.png")
    length = (left.shape[0]//left.shape[1])*10
    left = cv2.resize(left,(margin,length))
    top = cv2.rotate(left,cv2.ROTATE_90_CLOCKWISE)
    bottom = cv2.rotate(left,cv2.ROTATE_90_COUNTERCLOCKWISE)
    right = cv2.rotate(left,cv2.ROTATE_180)

    # Drawing left & right boundary
    n = (height//length)+1
    overflowy = int(((height/length)-(height//length))*length)
    y=0
    for i in range(n):
        if i == n-1:
            maze[y:(y+overflowy),0:margin,:] = left[0:overflowy,0:margin,:]
            maze[y:(y+overflowy),(width-margin):width,:] = right[0:overflowy,0:margin,:]
        else:
            maze[y:(y+length),0:margin,:] = left
            maze[y:(y+length),(width-margin):width,:] = right
        y = y+length

    # Drawing top & bottom boundary
    offset = margin*.8
    n = ((width-(2*offset))//length)+1
    overflowx = int((((width-(2*offset))/length)-((width-(2*offset))//length))*length)
    x=int(offset)
    for i in range(int(n)):
        if i == n-1:
            maze[0:margin,x:(x+overflowx),:] = top[0:margin,0:overflowx,:]
            maze[(height-margin):height,x:(x+overflowx),:] = bottom[0:margin,0:overflowx,:]
        else:
            maze[0:margin,x:(x+length),:] = top
            maze[(height-margin):height,x:(x+length),:] = bottom
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


def animate(maze, loki, path, steps, adjustedBoxWidth):
    path = calculatePoints(path, adjustedBoxWidth)
    depth = margin-2
    width = (adjustedBoxWidth>>1)+depth
    floki = np.zeros((loki.shape[0]+(depth<<1), loki.shape[1]+(depth<<1), 3), np.uint8)
    floki[depth:(depth+loki.shape[0]), depth:(depth+loki.shape[1]), :] = loki
    for dir, point, dst in path:
        shift = (dst*adjustedBoxWidth)//steps
        x, y = point

        for i in range(steps):
            if dir == 'left':
                x = x-shift
            if dir == 'right':
                x = x+shift
            if dir == 'up':
                y = y-shift
            elif dir == 'down':
                y = y+shift

            #################################
            roi = maze[(y-width):(y+width), (x-width):(x+width), :]
            result = addObject(roi.copy(),floki,10)
            cv2.line(maze, point, (x,y), (245,117,170), 2)
            fmaze = maze.copy()
            fmaze[(y-width):(y+width), (x-width):(x+width), :] = result
            #################################
            cv2.imshow("TREASURE HUNTER",fmaze)
            k = cv2.waitKey(13)
            if k == ord('q'):
                cv2.destroyAllWindows()
                return
            elif k == ord(' '):
                l = cv2.waitKey(0)
                if l == ord('q'):
                    cv2.destroyAllWindows()
                    return
                elif l == ord(' '):
                    pass
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def calculatePoints(path, adjustedBoxWidth):
    points = []
    for i,point in enumerate(path):
        x = margin + (point[0]*adjustedBoxWidth) + (adjustedBoxWidth>>1)
        y = margin + (point[1]*adjustedBoxWidth) + (adjustedBoxWidth>>1)
        if i<len(path)-1:
            diff_x = point[0]-path[i+1][0]
            diff_y = point[1]-path[i+1][1]
            if diff_x<0 and diff_y==0:          #right
                points.append(("right",(x,y),(-diff_x)))
            elif diff_x>0 and diff_y==0:        #left
                points.append(("left",(x,y),diff_x))
            elif diff_x==0 and diff_y>0:        #up
                points.append(("up",(x,y),diff_y))
            elif diff_x==0 and diff_y<0:        #down
                points.append(("down",(x,y),(-diff_y)))
    return points


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\nWARNING!!! Please mention Maze File Name")
    else:
        img = generateImage(sys.argv)
        cv2.namedWindow("TREASURE HUNTER")
        cv2.imshow("TREASURE HUNTER",img)
        cv2.waitKey(0)