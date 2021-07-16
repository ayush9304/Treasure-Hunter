import sys
import cv2
import numpy as np

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap, QImage, QIntValidator
from PySide6 import QtCore
from PySide6.QtCore import QThread, Signal

from ui_design import Ui_MainWindow
from displayImage import generateImage

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.height_input.setValidator(QIntValidator(5,100))
        self.ui.width_input.setValidator(QIntValidator(1,200))

        self.ui.generateMazeBtn.clicked.connect(self.generateMaze)
        self.ui.solveMazeBtn.clicked.connect(self.clicked)
        

        self.show()

    def clicked(self):
        self.ui.displayMazeLabel.setText('<p style="font-size: 11pt;">Not implemented yet.</font>')

    def generateMaze(self):
        self.ui.displayMazeLabel.setText('<p style="font-size:11pt;">Generating maze...</font>')
        self.ui.generateMazeBtn.setEnabled(False)
        width = int(self.ui.width_input.text())
        height = int(self.ui.height_input.text())

        self.generatorWorker = generateMazeWorker(width, height)
        self.generatorWorker.start()
        self.generatorWorker.response.connect(self.updateImage)

    def updateImage(self, maze, maze_ws, fromf):
        if fromf == "generator":
            self.ui.generateMazeBtn.setEnabled(True)
            self.generatorWorker.stop()
        elif fromf == 'solver':
            self.ui.solveMazeBtn.setEnabled(True)
        self.maze = maze
        self.maze_ws = maze_ws
        img = QImage(maze,self.maze.shape[1],self.maze.shape[0],self.maze.strides[0],QImage.Format_BGR888)

        if maze.shape[1] <= 725 and maze.shape[0] <= 425:
            self.ui.displayMazeLabel.setScaledContents(False)
            self.ui.displayMazeLabel.setPixmap(QPixmap(img))
        elif 1.4006 <= (maze.shape[1]/maze.shape[0]) <= 2.133:
            self.ui.displayMazeLabel.setScaledContents(True)
            self.ui.displayMazeLabel.setPixmap(QPixmap(img))
        else:
            self.ui.displayMazeLabel.setScaledContents(False)
            img = img.scaled(951,581,QtCore.Qt.KeepAspectRatio)
            self.ui.displayMazeLabel.setPixmap(QPixmap(img))


class generateMazeWorker(QThread):
    response = Signal(np.ndarray,np.ndarray,str)

    def __init__(self, width, height):
        super(generateMazeWorker, self).__init__()
        self.width = width
        self.height = height
    
    def run(self):
        # Random maze generator will be inserted below
        ###############################################################################---v
        #from game import getMazeData
        #self.mazeMatrix = getMazeData()
        import RMC
        self.mazeMatrix = RMC.getMaze(self.width, self.height)
        ###############################################################################---^
        self.maze, self.maze_ws = generateImage(self.mazeMatrix)
        self.response.emit(self.maze, self.maze_ws, 'generator')

    def stop(self):
        self.quit()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())
