#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QComboBox, QLabel
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit
from PyQt5.QtCore import QSize
import time
import serial
import serial.tools.list_ports

patternlist = ['Базовый', 'Проектный']
grouplist = ['Космо', 'Робо', 'Био', 'Жора', 'etc.']


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def button1(self):
        self.commandLabel.clear()
        self.commandLabel.setText("There is function numba uan.\n")

    def button2(self):
        self.commandLabel.clear()
        self.commandLabel.setText("Func num 2.\n")

    def button3(self):
        self.commandLabel.clear()
        self.commandLabel.setText("3.\n")

    def button4(self):
        self.commandLabel.clear()
        self.commandLabel.setText("This is the last func.\n")

    def initUI(self):
        self.commandLabel = QLabel(self)
        self.commandLabel.setText("Command line")
        self.commandLabel.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.commandLabel.resize(635, 25)


        self.patternLabel = QLabel(self)
        self.patternLabel.setText('Pattern: ')
        self.patternLabel.move(5, 45)
        self.patternLabel.resize(125, 32)
        self.patternLabel.setAlignment(Qt.AlignRight)
        self.patternLabel.setFont(QtGui.QFont('SansSerif', 20))

        patternCombo = QComboBox(self)
        patternCombo.resize(100, 25)
        patternCombo.move(150, 55)
        patternCombo.addItems(patternlist)

        pattern_acceptButton = QPushButton('√', self)
        pattern_acceptButton.clicked.connect(self.button1)
        pattern_acceptButton.move(270, 55)
        pattern_acceptButton.resize(26, 26)


        self.groupLabel = QLabel(self)
        self.groupLabel.setText('Group: ')
        self.groupLabel.move(5, 190)
        self.groupLabel.resize(125, 32)
        self.groupLabel.setAlignment(Qt.AlignRight)
        self.groupLabel.setFont(QtGui.QFont('SansSerif', 20))

        groupCombo = QComboBox(self)
        groupCombo.move(150, 200)
        groupCombo.addItems(grouplist)
        groupCombo.resize(100, 25)

        group_acceptButton = QPushButton('√', self)
        group_acceptButton.clicked.connect(self.button2)
        group_acceptButton.move(270, 200)
        group_acceptButton.resize(26, 26)


        printButton = QPushButton('Function button3', self)
        printButton.clicked.connect(self.button3)
        printButton.resize(600, 120)
        printButton.move(20, 340)

        
        # qbtn5 = QPushButton('Выход', self)
        # qbtn5.clicked.connect(QCoreApplication.instance().quit)
        # qbtn5.move(60, 200)


        self.setWindowTitle('AuroraBorealis: Печать дипломов')
        self.setFixedSize(640, 480)
        # self.move(0, 0)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
