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
from pathlib import Path
from WordTemplate.WordTemplateCombine import wordTemplateCombine
from WordTemplate.WordTemplateRapid import wordTemplateRapid

patternlist = ['base', 'project']
grouplist = os.listdir('lists')
pattern = 'base'
group_check = False


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
        global group, group_check
        self.commandLabel.clear()
        group = self.groupCombo.currentText()
        self.commandLabel.setText("Group " + group + " has succesfully set...")
        print(self.groupCombo.currentText())
        group_check = True


    def button3(self):
        self.commandLabel.clear()
        print(self.templateBox.isChecked())
        if group_check:
            if self.templateBox.isChecked():
                wordTemplateCombine(group=group, pattern=pattern)
            else:
                wordTemplateRapid(group=group, pattern=pattern)
            i = str(len(os.listdir(Path("diplomas"))))
            self.printedLable.setText("Подготовлено дипломов: " + i)
            self.commandLabel.setText("Дипломы успешно напечатаны...")
        else:
            self.printedLable.setText('Вы не выбрали group')

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
        self.groupLabel.move(15, 120)
        self.groupLabel.resize(125, 32)
        self.groupLabel.setFont(QtGui.QFont('SansSerif', 20, QtGui.QFont.Bold))

        self.groupCombo = QComboBox(self)
        self.groupCombo.move(135, 130)
        self.groupCombo.addItems(grouplist)
        self.groupCombo.resize(420, 25)

        group_acceptButton = QPushButton('√', self)
        group_acceptButton.clicked.connect(self.button2)
        group_acceptButton.move(580, 130)
        group_acceptButton.resize(26, 26)


        self.printedLable = QLabel(self)
        self.printedLable.move(20, 400)
        self.printedLable.resize(480, 34)
        self.printedLable.setFont(QtGui.QFont('SansSerif', 20, QtGui.QFont.Bold))


        printButton = QPushButton('Подготовить дипломы', self)
        printButton.clicked.connect(self.button3)
        printButton.resize(600, 120)
        printButton.move(15, 465)

        self.templateBox = QCheckBox('Сохранить дипломы в 1 файл?', self)
        self.templateBox.move(15, 200)
        self.templateBox.setFont(QtGui.QFont('SansSerif', 16, QtGui.QFont.Bold))

        
        # qbtn5 = QPushButton('Выход', self)
        # qbtn5.clicked.connect(QCoreApplication.instance().quit)
        # qbtn5.move(60, 200)


        self.setWindowTitle('AuroraBorealis: Печать дипломов')
        self.setFixedSize(1152, 600)
        # self.move(0, 0)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
