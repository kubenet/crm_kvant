#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QComboBox
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

    def start_tem(self):
        self.plain.insertPlainText("Пульт управления ТЕМ-камерой:\nВывод информации от внутренних подсистем:\n")

    def button1(self):
        self.plain.insertPlainText("There is function numba uan.\n")

    def button2(self):
        self.plain.insertPlainText("Func num 2.\n")

    def button3(self):
        self.plain.insertPlainText("3.\n")

    def button4(self):
        self.plain.insertPlainText("This is the last func.\n")

    def initUI(self):
        # Add text field
        self.plain = QPlainTextEdit(self)
        self.plain.insertPlainText("Пульт управления ТЕМ-камерой:\nВывод информации от внутренних подсистем:\n")
        self.plain.insertPlainText("system ON:\n")
        self.plain.move(200, 20)
        self.plain.resize(400, 200)

        qbtn1 = QPushButton('Func start_tem, inside', self)
        qbtn1.clicked.connect(self.start_tem)
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



        #self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Пульт управления TEM-камерой')
        # привязка к разрешению экрана
        desktop = QApplication.desktop()
        screen01 = desktop.primaryScreen() # у меня 2 монитора, определяем главный
        # получаем разрешение нужного монитора
        res = desktop.screenGeometry(screen01)
        # устанавливаем размер откна по размеру монитора
        self.setFixedSize(res.width(), res.height())
        # перемещаем окно чтобы оно заняло весь монитор
        self.move(0, 0)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
