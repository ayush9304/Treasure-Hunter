# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_designOZDCHs.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1274, 640)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1274, 617))
        MainWindow.setMaximumSize(QSize(1274, 6170))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(40, 44, 52, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(227, 227, 227, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(160, 160, 160, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush5 = QBrush(QColor(105, 105, 105, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        brush6 = QBrush(QColor(0, 120, 215, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush6)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        brush7 = QBrush(QColor(0, 0, 255, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Link, brush7)
        brush8 = QBrush(QColor(255, 0, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush8)
        brush9 = QBrush(QColor(245, 245, 245, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush9)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.NoRole, brush10)
        brush11 = QBrush(QColor(255, 255, 220, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush12 = QBrush(QColor(0, 0, 0, 128))
        brush12.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        brush13 = QBrush(QColor(240, 240, 240, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush9)
        brush14 = QBrush(QColor(0, 0, 0, 255))
        brush14.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.NoRole, brush14)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        brush15 = QBrush(QColor(120, 120, 120, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush15)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        brush16 = QBrush(QColor(247, 247, 247, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush16)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush15)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush15)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        brush17 = QBrush(QColor(0, 0, 0, 255))
        brush17.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.NoRole, brush17)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        MainWindow.setPalette(palette)
        icon = QIcon()
        icon.addFile(u"img/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	background: #282c34;\n"
"}\n"
"QGroupBox{\n"
"	border: 1px solid #3e4656;/*#f89dcd;#bd93f9;*/\n"
"	border-radius: 5px;\n"
"	color: #ffffff;\n"
"	margin-top: 0.5em;\n"
"}\n"
"QGroupBox::title {\n"
"	padding-top: -16px;\n"
"    left: 10px;\n"
"}\n"
"QLabel{\n"
"	color: #ffffff;\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(189, 147, 249);\n"
"	border-radius: 2px;\n"
"	color: #ffffff;\n"
"	font-size: 2em;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #ff79c6;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"	color: #ffffff;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.displayMazeLabel = QLabel(self.centralwidget)
        self.displayMazeLabel.setObjectName(u"displayMazeLabel")
        self.displayMazeLabel.setGeometry(QRect(20, 30, 951, 581))
        font = QFont()
        font.setPointSize(11)
        self.displayMazeLabel.setFont(font)
        self.displayMazeLabel.setCursor(QCursor(Qt.CrossCursor))
        self.displayMazeLabel.setAutoFillBackground(False)
        self.displayMazeLabel.setStyleSheet(u"QLabel{\n"
"	background:#21252b;\n"
"	border: 1px solid #bd93f9;\n"
"	border-radius: 5px;\n"
"	padding: 1px;\n"
"}")
        self.displayMazeLabel.setFrameShape(QFrame.StyledPanel)
        self.displayMazeLabel.setFrameShadow(QFrame.Raised)
        self.displayMazeLabel.setTextFormat(Qt.AutoText)
        self.displayMazeLabel.setScaledContents(False)
        self.displayMazeLabel.setAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(990, 50, 261, 261))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.groupBox.setPalette(palette1)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet(u"")
        self.groupBox.setFlat(False)
        self.generateMazeBtn = QPushButton(self.groupBox)
        self.generateMazeBtn.setObjectName(u"generateMazeBtn")
        self.generateMazeBtn.setGeometry(QRect(20, 210, 221, 31))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.generateMazeBtn.setFont(font1)
        self.generateMazeBtn.setFocusPolicy(Qt.WheelFocus)
        self.generateMazeBtn.setAutoDefault(True)
        self.generateMazeBtn.setFlat(False)
        self.height_label = QLabel(self.groupBox)
        self.height_label.setObjectName(u"height_label")
        self.height_label.setGeometry(QRect(20, 110, 221, 31))
        self.width_label = QLabel(self.groupBox)
        self.width_label.setObjectName(u"width_label")
        self.width_label.setGeometry(QRect(20, 20, 221, 31))
        self.width_input = QLineEdit(self.groupBox)
        self.width_input.setObjectName(u"width_input")
        self.width_input.setGeometry(QRect(20, 50, 221, 31))
        self.width_input.setFocusPolicy(Qt.WheelFocus)
        self.width_input.setInputMethodHints(Qt.ImhDigitsOnly)
        self.width_input.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.width_input.setClearButtonEnabled(True)
        self.height_input = QLineEdit(self.groupBox)
        self.height_input.setObjectName(u"height_input")
        self.height_input.setGeometry(QRect(20, 140, 221, 31))
        self.height_input.setFocusPolicy(Qt.WheelFocus)
        self.height_input.setInputMethodHints(Qt.ImhDigitsOnly)
        self.height_input.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.height_input.setClearButtonEnabled(True)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(990, 340, 261, 121))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Highlight, brush6)
        palette2.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Link, brush7)
        palette2.setBrush(QPalette.Active, QPalette.LinkVisited, brush8)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush9)
        palette2.setBrush(QPalette.Active, QPalette.NoRole, brush)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Highlight, brush13)
        palette2.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Link, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush9)
        brush18 = QBrush(QColor(0, 0, 0, 255))
        brush18.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Inactive, QPalette.NoRole, brush18)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush16)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Highlight, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Link, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        brush19 = QBrush(QColor(0, 0, 0, 255))
        brush19.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Disabled, QPalette.NoRole, brush19)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.groupBox_2.setPalette(palette2)
        self.groupBox_2.setStyleSheet(u"")
        self.solveMazeBtn = QPushButton(self.groupBox_2)
        self.solveMazeBtn.setObjectName(u"solveMazeBtn")
        self.solveMazeBtn.setGeometry(QRect(20, 50, 221, 31))
        self.solveMazeBtn.setFont(font1)
        self.solveMazeBtn.setFocusPolicy(Qt.WheelFocus)
        self.solveMazeBtn.setAutoDefault(True)
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.width_input, self.height_input)
        QWidget.setTabOrder(self.height_input, self.generateMazeBtn)
        QWidget.setTabOrder(self.generateMazeBtn, self.solveMazeBtn)

        self.retranslateUi(MainWindow)

        self.generateMazeBtn.setDefault(False)
        self.solveMazeBtn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Treasure Hunter", None))
        self.displayMazeLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#ff79c6;\">TREASURE HUNTER</span></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Maze Generator", None))
#if QT_CONFIG(tooltip)
        self.generateMazeBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.generateMazeBtn.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.height_label.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.width_label.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Maze Solver", None))
        self.solveMazeBtn.setText(QCoreApplication.translate("MainWindow", u"Solve", None))
    # retranslateUi

