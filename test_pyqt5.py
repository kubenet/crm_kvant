#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QComboBox, QLabel
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit
from PyQt5.QtCore import QSize
import time
import serial
import serial.tools.list_ports

x=['1, 2, 3', 'stroke']


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def button1(self):
        self.commandstroke.clear()
        self.commandstroke.setText("There is function numba uan.\n")


    def button2(self):
        self.commandstroke.clear()
        self.commandstroke.setText("Func num 2.\n")

    def button3(self):
        self.commandstroke.clear()
        self.commandstroke.setText("3.\n")

    def button4(self):
        self.commandstroke.clear()
        self.commandstroke.setText("This is the last func.\n")

    def initUI(self):
        self.commandstroke = QLabel(self)
        self.commandstroke.setAlignment(QtCore.Qt.AlignRight)
        self.commandstroke.setText("Program started...")
        self.commandstroke.move(0, 10)
        self.commandstroke.resize(635, 25)

        self.patternlabel = QLabel(self)
        self.patternlabel.setText("Шаблон: ")
        self.patternlabel.move(200, 50)
        self.patternlabel.setFont(QtGui.QFont("Times", 24, QtGui.QFont.Bold))

        patterncombo = QComboBox(self)
        patterncombo.resize(150, 26)
        patterncombo.move(355, 60)
        patterncombo.addItems(x)

        self.listslabel = QLabel(self)
        self.listslabel.setText("Список: ")
        self.listslabel.move(217, 150)
        self.listslabel.setFont(QtGui.QFont("Times", 24, QtGui.QFont.Bold))

        listscombo = QComboBox(self)
        listscombo.resize(150, 26)
        listscombo.move(355, 160)
        listscombo.addItems(x)

        qbtn1 = QPushButton('Function button1', self)
        qbtn1.clicked.connect(self.button1)
        qbtn1.move(60, 50)

        qbtn2 = QPushButton('Function button2', self)
        qbtn2.clicked.connect(self.button2)
        qbtn2.move(60, 110)

        qbtn3 = QPushButton('Function button3', self)
        qbtn3.clicked.connect(self.button3)
        qbtn3.move(60, 140)

        qbtn4 = QPushButton('Function button4', self)
        qbtn4.clicked.connect(self.button4)
        qbtn4.move(60, 170)

        combo = QComboBox(self)
        combo.move(60, 80)
        combo.addItems(x)

        qbtn5 = QPushButton('Выход', self)
        qbtn5.clicked.connect(QCoreApplication.instance().quit)
        qbtn5.move(60, 200)


        self.setFixedSize(640, 480)
        self.setWindowTitle('Печать дипломов')

        # self.setStyleSheet("background-color:")
        #
        # desktop = QApplication.desktop()
        # screen01 = desktop.primaryScreen()
        # res = desktop.screenGeometry(screen01)

        self.move(0, 0)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
