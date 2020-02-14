#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
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
from pathlib import Path
from WordTemplate.WordTemplateCombine import wordTemplateCombine
from WordTemplate.WordTemplateRapid import wordTemplateRapid

patternlist = ['base', 'project']
grouplist = os.listdir('lists')


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def button1(self):
        global pattern
        self.commandLabel.clear()
        pattern = self.patternCombo.currentText()
        self.commandLabel.setText("Pattern " + pattern + " has succesfully set...")
        print(self.patternCombo.currentText())

    def button2(self):
        global group
        self.commandLabel.clear()
        group = self.groupCombo.currentText()
        self.commandLabel.setText("Group " + group + " has succesfully set...")
        print(self.groupCombo.currentText())


    def button3(self):
        self.commandLabel.clear()
        self.commandLabel.setText("Дипломы успешно напечатаны...")
        wordTemplateRapid(group=group, pattern=pattern)
        i = str(len(os.listdir(Path("diplomas"))))
        self.printedLable.setText("Напечатано дипломов: " + i)


    def initUI(self):
        self.commandLabel = QLabel(self)
        self.commandLabel.setText("Command line. Program started...")
        self.commandLabel.setAlignment(Qt.AlignRight)
        self.commandLabel.resize(635, 25)


        self.patternLabel = QLabel(self)
        self.patternLabel.setText('Pattern: ')
        self.patternLabel.move(5, 45)
        self.patternLabel.resize(125, 32)
        self.patternLabel.setAlignment(Qt.AlignRight)
        self.patternLabel.setFont(QtGui.QFont('SansSerif', 20, QtGui.QFont.Bold))

        self.patternCombo = QComboBox(self)
        self.patternCombo.resize(100, 25)
        self.patternCombo.move(135, 55)
        self.patternCombo.addItems(patternlist)

        pattern_acceptButton = QPushButton('√', self)
        pattern_acceptButton.clicked.connect(self.button1)
        pattern_acceptButton.move(255, 55)
        pattern_acceptButton.resize(26, 26)


        self.groupLabel = QLabel(self)
        self.groupLabel.setText('Group: ')
        self.groupLabel.move(5, 190)
        self.groupLabel.resize(125, 32)
        self.groupLabel.setAlignment(Qt.AlignRight)
        self.groupLabel.setFont(QtGui.QFont('SansSerif', 20, QtGui.QFont.Bold))

        self.groupCombo = QComboBox(self)
        self.groupCombo.move(135, 200)
        self.groupCombo.addItems(grouplist)
        self.groupCombo.resize(420, 25)

        group_acceptButton = QPushButton('√', self)
        group_acceptButton.clicked.connect(self.button2)
        group_acceptButton.move(580, 200)
        group_acceptButton.resize(26, 26)


        self.printedLable = QLabel(self)
        self.printedLable.move(20, 280)
        self.printedLable.resize(480, 34)
        self.printedLable.setFont(QtGui.QFont('SansSerif', 20, QtGui.QFont.Bold))


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
