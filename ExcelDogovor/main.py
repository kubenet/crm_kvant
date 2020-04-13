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
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit, QCheckBox
from PyQt5.QtCore import QSize
import time
from ExcelDefs.ExcelStudentFiller import xlStudFiller

grouplist = os.listdir('lists')

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def button1(self):
        self.printedLable.setText("Договор подготовлен")
        self.commandLabel.setText("Договор успешно подготовлен...")

    def button2(self):
        global group
        group = self.groupCombo.currentText()
        self.studentLabel.setText('Student: ')
        self.student_acceptButton.resize(26, 26)
        self.studentCombo.addItems(xlStudFiller(group))
        self.studentCombo.resize(400, 25)
        self.commandLabel.setText("Группа выбрана успешно...")

    def button3(self):
        pass

    def initUI(self):
        self.commandLabel = QLabel(self)
        self.commandLabel.setText("Command line. Program started...")
        self.commandLabel.setAlignment(Qt.AlignRight)
        self.commandLabel.move(0, 2)
        self.commandLabel.resize(1147, 25)


        self.groupLabel = QLabel(self)
        self.groupLabel.setText('Group: ')
        self.groupLabel.move(15, 45)
        self.groupLabel.resize(125, 32)
        self.groupLabel.setFont(QtGui.QFont('SansSerif', 20, QtGui.QFont.Bold))
        group_acceptButton = QPushButton('√', self)
        group_acceptButton.clicked.connect(self.button2)
        group_acceptButton.move(580, 55)
        group_acceptButton.resize(26, 26)
        self.groupCombo = QComboBox(self)
        self.groupCombo.resize(400, 25)
        self.groupCombo.move(140, 55)
        self.groupCombo.addItems(grouplist)


        self.studentLabel = QLabel(self)
        self.studentLabel.move(15, 120)
        self.studentLabel.resize(125, 32)
        self.studentLabel.setFont(QtGui.QFont('SansSerif', 20, QtGui.QFont.Bold))
        self.student_acceptButton = QPushButton('√', self)
        self.student_acceptButton.clicked.connect(self.button3)
        self.student_acceptButton.move(580, 130)
        self.student_acceptButton.resize(0, 0)
        self.studentCombo = QComboBox(self)
        self.studentCombo.move(140, 130)
        self.studentCombo.resize(0, 0)


        self.printedLable = QLabel(self)
        self.printedLable.move(20, 400)
        self.printedLable.resize(480, 34)
        self.printedLable.setFont(QtGui.QFont('SansSerif', 20, QtGui.QFont.Bold))

        printButton = QPushButton('Подготовить договор', self)
        printButton.clicked.connect(self.button1)
        printButton.resize(600, 120)
        printButton.move(15, 465)

        self.setWindowTitle('AuroraBorealis: Печать договоров')
        self.setFixedSize(1152, 600)
        # self.move(0, 0)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
