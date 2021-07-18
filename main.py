import sys
import cv2
import numpy as np
import time

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap, QImage, QIntValidator, QIcon
from PySide6 import QtCore
from PySide6.QtCore import QThread, Signal, QSize, QCoreApplication

from ui_design import Ui_MainWindow
from displayImage import generateImage, addObject
import displayParameters
import mazeGenerator
import bfs

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.height_input.setValidator(QIntValidator(5,100))
        self.ui.width_input.setValidator(QIntValidator(1,200))

        self.ui.generateMazeBtn.clicked.connect(self.generateMaze)
        self.ui.solveMazeBtn.clicked.connect(self.solveMaze)

        self.mazeMatrix = None
        self.maze = None
        self.maze_ws = None
        self.disp_maze = None
        self.loki = None
        self.margin = displayParameters.margin
        self.steps = displayParameters.steps

        self.show()

    def solveMaze(self):
        self.ui.solveMazeBtn.setEnabled(False)

        if self.maze is None or self.mazeMatrix is None:
            popup("Please generate a maze first","Information")
            self.ui.solveMazeBtn.setEnabled(True)
            return
        elif self.maze_ws is None:
            popup("Maze data has been corrupted.\nPlease regenerate maze.","Critical")
            self.ui.solveMazeBtn.setEnabled(True)
            return

        self.ui.displayMazeLabel.setText('<p style="font-size: 11pt;">Solving maze...</font>')
        
        self.solverWorker = solveMazeWorker(self.mazeMatrix, self.maze_ws.copy(), self.loki, self.boxWidth, self.margin, self.steps)
        self.solverWorker.start()
        self.solverWorker.response.connect(self.updateImage)

    def generateMaze(self):
        self.ui.generateMazeBtn.setEnabled(False)
        try:
            width = int(self.ui.width_input.text())
            height = int(self.ui.height_input.text())
        except:
            popup("Please mention width/height of maze","Information")
            self.ui.generateMazeBtn.setEnabled(True)
            return

        if(width<3 or height<3):
            popup("Width / Height value of maze should be atleast 3","Information")
            self.ui.generateMazeBtn.setEnabled(True)
            return

        self.ui.displayMazeLabel.setText('<p style="font-size:11pt;">Generating maze...</font>')

        self.generatorWorker = generateMazeWorker(width, height)
        self.generatorWorker.start()
        self.generatorWorker.response.connect(self.updateImage)

    def updateImage(self, error, whatError, disp_maze, fromf, lastResponse=True, mazeMatrix = None, maze=None, maze_ws=None, loki=None, boxWidth=None):
        
        if fromf == "generator":
            if error:
                if whatError == "RecursionError":
                    popup("Exceeded maximum maze size limit\nPlease reduce the size of maze","Critical")
                else:
                    popup(whatError,"Critical")
                self.ui.generateMazeBtn.setEnabled(True)
            else:
                self.ui.generateMazeBtn.setEnabled(True)
                self.generatorWorker.stop()
                
                try:
                    if self.solverWorker:
                        self.solverWorker.stopFlag = True
                        self.ui.solveMazeBtn.setEnabled(True)
                except:
                    pass
                
                self.maze = maze
                self.maze_ws = maze_ws
                self.loki = loki
                self.boxWidth = boxWidth
                self.mazeMatrix = mazeMatrix
        elif fromf == 'solver':
            if error:
                popup(whatError,"Critical")
                self.ui.solveMazeBtn.setEnabled(True)
            else:
                if lastResponse:
                    self.ui.solveMazeBtn.setEnabled(True)
        
        if disp_maze is None:
            if self.disp_maze is None:
                if self.maze is None:
                    self.ui.displayMazeLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#ff79c6;\">TREASURE HUNTER</span></p></body></html>", None))
                else:
                    disp_maze = self.maze.copy()
            else:
                disp_maze = self.disp_maze.copy()
        
        self.disp_maze = disp_maze
        img = QImage(self.disp_maze,self.disp_maze.shape[1],self.disp_maze.shape[0],self.disp_maze.strides[0],QImage.Format_BGR888)
        if self.disp_maze.shape[1] <= 725 and self.disp_maze.shape[0] <= 425:
            self.ui.displayMazeLabel.setScaledContents(False)
            self.ui.displayMazeLabel.setPixmap(QPixmap(img))
        elif 1.4006 <= (self.disp_maze.shape[1]/self.disp_maze.shape[0]) <= 2.133:
            self.ui.displayMazeLabel.setScaledContents(True)
            self.ui.displayMazeLabel.setPixmap(QPixmap(img))
        else:
            self.ui.displayMazeLabel.setScaledContents(False)
            img = img.scaled(951,581,QtCore.Qt.KeepAspectRatio)
            self.ui.displayMazeLabel.setPixmap(QPixmap(img))



class generateMazeWorker(QThread):
    response = Signal(bool,str,np.ndarray,str,bool,list,np.ndarray,np.ndarray,np.ndarray,int)

    def __init__(self, width, height):
        super(generateMazeWorker, self).__init__()
        self.width = width
        self.height = height
    
    def run(self):
        try:
            start = time.time()
            
            mazeClass = mazeGenerator.Maze(self.width, self.height)
            self.mazeMatrix = mazeClass.matrix()
            
            self.maze, self.maze_ws, self.loki, self.boxWidth = generateImage(self.mazeMatrix)
            self.response.emit(False, None, self.maze, 'generator', True, self.mazeMatrix, self.maze, self.maze_ws, self.loki, self.boxWidth)
            end = time.time()
            print(f"Generate Maze Time: {end-start}s")
        except RecursionError:
            self.response.emit(True, "RecursionError", None, "generator", None, None, None, None, None, None)
        except Exception as e:
            self.response.emit(True, str(e), None, "generator", None, None, None, None, None, None)

    def stop(self):
        self.quit()

class solveMazeWorker(QThread):
    response = Signal(bool, str, np.ndarray, str, bool)

    def __init__(self, mazeMatrix, maze_ws, loki, adjustedBoxWidth, margin, steps):
        super(solveMazeWorker, self).__init__()
        self.mazeMatrix = mazeMatrix
        self.maze = maze_ws
        self.boxWidth = adjustedBoxWidth
        self.margin = margin
        self.loki = loki
        self.steps = steps
        self.stopFlag = False

    def run(self):
        try:
            start = time.time()
        
            row = len(self.mazeMatrix)
            col = len(self.mazeMatrix[1])
            _, self.path = bfs.bfs(self.mazeMatrix.copy(), row, col)

            self.path_points = self.calculatePoints()
            depth = self.margin-2
            width = (self.boxWidth>>1)+depth
            fmaze = None
            floki = np.zeros((self.loki.shape[0]+(depth<<1), self.loki.shape[1]+(depth<<1), 3), np.uint8)
            floki[depth:(depth+self.loki.shape[0]), depth:(depth+self.loki.shape[1]), :] = self.loki
            for dir, point, dst in self.path_points:
                if not self.stopFlag:
                    shift = (dst*self.boxWidth)//self.steps
                    x, y = point

                    for i in range(self.steps):
                        if dir == 'left':
                            x = x-shift
                        if dir == 'right':
                            x = x+shift
                        if dir == 'up':
                            y = y-shift
                        elif dir == 'down':
                            y = y+shift

                        roi = self.maze[(y-width):(y+width), (x-width):(x+width), :]
                        result = addObject(roi.copy(),floki,10)
                        cv2.line(self.maze, point, (x,y), (245,117,170), 2)
                        fmaze = self.maze.copy()
                        fmaze[(y-width):(y+width), (x-width):(x+width), :] = result
                
                        if not self.stopFlag:
                            self.response.emit(False, None, fmaze, 'solver', False)
                            cv2.waitKey(13)
                        else:
                            return
                else:
                    return
            
            if not self.stopFlag:
                self.response.emit(False, None, fmaze, 'solver', True)

                end = time.time()
                print(f"Solve Maze Time: {(end-start)}")
        except Exception as e:
            self.response.emit(True, str(e), None, 'solver', None)
        
        self.stop()

    def calculatePoints(self):
        points = []
        for i,point in enumerate(self.path):
            x = self.margin + (point[0]*self.boxWidth) + (self.boxWidth>>1)
            y = self.margin + (point[1]*self.boxWidth) + (self.boxWidth>>1)
            if i<len(self.path)-1:
                diff_x = point[0]-self.path[i+1][0]
                diff_y = point[1]-self.path[i+1][1]
                if diff_x<0 and diff_y==0:          #right
                    points.append(("right",(x,y),(-diff_x)))
                elif diff_x>0 and diff_y==0:        #left
                    points.append(("left",(x,y),diff_x))
                elif diff_x==0 and diff_y>0:        #up
                    points.append(("up",(x,y),diff_y))
                elif diff_x==0 and diff_y<0:        #down
                    points.append(("down",(x,y),(-diff_y)))
        return points

    def stop(self):
        self.quit()


def popup(message,type):
        msg = QMessageBox()
        icon = QIcon()
        icon.addFile(u"img/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setWindowTitle("Treasure Hunter")

        if type == "Information":
            msg.setIcon(QMessageBox.Information)
        elif type == "Warning":
            msg.setIcon(QMessageBox.Warning)
        elif type == "Critical":
            msg.setIcon(QMessageBox.Critical)
        elif type == "Question":
            msg.setIcon(QMessageBox.Question)
        
        msg.setText(message)
        msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec())
