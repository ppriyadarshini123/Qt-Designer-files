import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QDialogButtonBox

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("pizza_order.ui", self)

class Order_Details(QDialog):
    def __init__(self):
        super(Order_Details, self).__init__()
        loadUi("Order_Details.ui", self)

#main
app = QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
mainwindow=MainWindow()
order_details= Order_Details()
widget.addWidget(mainwindow)
widget.addWidget(order_details)
widget.setFixedHeight(300)
widget.setFixedWidth(400)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")