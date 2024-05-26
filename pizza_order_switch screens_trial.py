
# from PyQt5 import loadUi
# from PyQt5 import QtWidgets
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QDialog, QApplication
# import sys

from PyQt5.uic import loadUi #Loads a ui file
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QComboBox, QDialog,QApplication
import json, sys

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("pizza_order.ui", self)

class Screen2(QDialog):
    def __init__(self):
        super(Screen2,self).__init__()
        loadUi("Order Details.ui", self)

#main
app = QApplication(sys.argv)

try:
    sys.exit(app.exec_())
except:
    print("Exiting")