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
from ExcelDefs.ExcelStudentFiller import xlStudFiller, xlStudProd

grouplist = os.listdir('lists')
patternlist = os.listdir('Documents')

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def button_pechat(self):
        try:
            xlStudProd(group, student, pattern)
        except Exception as E:
            E = str(E)
            self.printedLable.setText("Произошла ошибка, смотрите в \nкомандную строку.")
            self.commandLabel.setText(E)
        else:
            self.printedLable.setText("Договор подготовлен")
            self.commandLabel.setText("Договор успешно подготовлен...")

    def button_pattern(self):
        global pattern
        pattern = self.patternCombo.currentText()
        print(pattern)
        self.commandLabel.setText("Документ pattern выбран успешно...")

    def button_group(self):
        global group
        group = self.groupCombo.currentText()
        print(group)
        self.studentLabel.setText('Student: ')
        self.student_acceptButton.resize(26, 26)
        self.studentCombo.clear()
        self.studentCombo.addItems(xlStudFiller(group))
        self.studentCombo.resize(400, 25)
        self.commandLabel.setText("Группа выбрана успешно...")

    def button_stud(self):
        global student
        student = self.studentCombo.currentText()
        print(student)
        self.commandLabel.setText("Студент(ка) выбран(а) успешно...")

    def initUI(self):
        self.commandLabel = QLabel(self)
        self.commandLabel.setText("Command line. Program started...")
        self.commandLabel.setAlignment(Qt.AlignRight)
        self.commandLabel.move(0, 2)
        self.commandLabel.resize(1147, 25)


        self.patternLabel = QLabel(self)
        self.patternLabel.setText('Pattern: ')
        self.patternLabel.move(15, 45)
        self.patternLabel.resize(125, 32)
        self.patternLabel.setFont(QtGui.QFont('SansSerif', 20, QtGui.QFont.Bold))
        pattern_acceptButton = QPushButton('√', self)
        pattern_acceptButton.clicked.connect(self.button_pattern)
        pattern_acceptButton.move(580, 55)
        pattern_acceptButton.resize(26, 26)
        self.patternCombo = QComboBox(self)
        self.patternCombo.resize(400, 25)
        self.patternCombo.move(140, 55)
        self.patternCombo.addItems(patternlist)


        self.groupLabel = QLabel(self)
        self.groupLabel.setText('Group: ')
        self.groupLabel.move(15, 120)
        self.groupLabel.resize(125, 32)
        self.groupLabel.setFont(QtGui.QFont('SansSerif', 20, QtGui.QFont.Bold))
        group_acceptButton = QPushButton('√', self)
        group_acceptButton.clicked.connect(self.button_group)
        group_acceptButton.move(580, 130)
        group_acceptButton.resize(26, 26)
        self.groupCombo = QComboBox(self)
        self.groupCombo.resize(400, 25)
        self.groupCombo.move(140, 130)
        self.groupCombo.addItems(grouplist)


        self.studentLabel = QLabel(self)
        self.studentLabel.move(15, 195)
        self.studentLabel.resize(125, 32)
        self.studentLabel.setFont(QtGui.QFont('SansSerif', 20, QtGui.QFont.Bold))
        self.student_acceptButton = QPushButton('√', self)
        self.student_acceptButton.clicked.connect(self.button_stud)
        self.student_acceptButton.move(580, 205)
        self.student_acceptButton.resize(0, 0)
        self.studentCombo = QComboBox(self)
        self.studentCombo.move(140, 205)
        self.studentCombo.resize(0, 0)


        self.printedLable = QLabel(self)
        self.printedLable.move(20, 380)
        self.printedLable.resize(480, 80)
        self.printedLable.setFont(QtGui.QFont('SansSerif', 20, QtGui.QFont.Bold))

        printButton = QPushButton('Подготовить договор', self)
        printButton.clicked.connect(self.button_pechat)
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
