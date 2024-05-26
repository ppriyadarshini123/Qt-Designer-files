# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pizza_order.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.uic import loadUi #Loads a ui file
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QComboBox, QDialog
import json
from Order_Details import Ui_Dialog

class Ui_MainWindow(object):

#     def loadDatainJSONFile():
#         #         string_JSON ="""
# #                {
# #        "orders": [
# #            {
# #                "pizza":{
# #                   "name":"Veggie Supreme",
# #                    "size":"small",
# #                    "delivery":"True",
# #                    "toppings":"Olives"
# #                },
# #                "client":{
# #                    "name": "Jane Doe",
# #                    "email": "janedoe@gmail.com",
# #                    "phone":"0768675667",
# #                    "age": 23
# #                }
# #            },
# #            {
# #                "pizza":{
# #                    "name":"Chicken",
# #                    "size":"large",
# #                    "delivery":"False",
# #                    "toppings":"Mushrooms"
# #                },
# #                "client":{
# #                    "name": "Payal P",
# #                    "email": "pp@gmail.com",
# #                    "phone":"0768455667",
# #                    "age": 34
# #                }
# #            }
# #            ]
# #    }
# #                     """
        
#         data_JSON =                 {
#             "orders": [
#                 {
#                     "pizza":{
#                         "name":"Margerita",
#                         "size":"small",
#                         "delivery":"True",
#                         "toppings":"Olives"
#                         },
#                      "client":{
#                          "name": "Jane Doe",
#                          "email": "janedoe@gmail.com",
#                          "phone":"0768675667",
#                          "age": 23
#                          }
#                          },
#                          {
#                     "pizza":{
#                         "name":"Chicken",
#                         "size":"large",
#                         "delivery":"False",
#                         "toppings":"Mushrooms"
#                     },
#                     "client":{
#                         "name": "Payal P",
#                         "email": "pp@gmail.com",
#                         "phone":"0768455667",
#                         "age": 34
#                     }
#                 }
#             ]
#     }
#         # with open('test.json','w') as file:
#         #     json.dump(data_JSON,file, indent=4)
#         #try:
#             #Convert the python dictionary data_JSON into string with JSOn format and store it in a variable        
#             #json_object = json.dumps(data_JSON, indent=4)

#         #data = json.loads(string_JSON)
#         #print(type(data))
#         #print(data)
#         #Write to a .json file - pizza_order.json
#         #with open("test.json", 'w') as file:
        
#         file = open('test.json','w')

#         try:
#             #data = json.load(file)
#             #file.write(string_JSON)
#             json.dump(data_JSON, file,indent=4)
#         finally:
#             file.close()


#             # Convert JSON string to dictionary
#             #data_dict = json.loads(data_JSON)
#             #json.dump(data_dict, file)
#             #print(data_dict["size"])
        
    def clicked(self):
        #print("clicked")
        #print(self.lineEdit.toPlainText())
        #print(self.comboBox.currentText())
        
        if self.radioButton.isChecked:
            text_size = self.radioButton.text()
        elif self.radioButton_2.isChecked:
            text_size = self.radioButton_2.text()
        elif self.radioButton_3.isChecked:
            text_size = self.radioButton_3.text()

        if self.radioButton_4.isChecked:
            text_delivery = self.radioButton_4.text()
        elif self.radioButton_5.isChecked:
            text_delivery = self.radioButton_5.text()

        #Append the following data to the existing test.json file
        new_order = {
            "pizza":{
                    "name":self.comboBox.currentText(),
                    "size":text_size,
                    "delivery":text_delivery,
                    "toppings":self.comboBox_2.currentText()
                    },
            "client":{
                "name": self.lineEdit.text(),
                "email": self.lineEdit_3.text(),
                "phone":self.lineEdit_2.text(),
                "age": self.lineEdit_4.text()
                }
        }

        with open('test.json', 'r+') as file:
            #First we load existing data into a dict.
            file_data = json.load(file)
            #Join new_order with file_data inside "orders"
            file_data["orders"].append(new_order)
            #Sets file's current position at offset
            file.seek(0)
            #convert back to json
            json.dump(file_data, file, indent=4)
        
        #app = QtWidgets.QApplication(sys.argv)
        Dialog = QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        ui.exec()
        #app.exec()
        #sys.exit(app.exec_())
        #loadUi("second_file.ui",self)





    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(712, 638)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 210, 151, 20))
        self.label_5.setObjectName("label_5")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 30, 421, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(140, 110, 421, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_6.addWidget(self.lineEdit_4)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(140, 250, 318, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        
        #Added code
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox.addItem('--None--')
        self.comboBox.addItem('Margerita')
        self.comboBox.addItem('Veggie Supreme')
        self.comboBox.addItem('Chicken')
        self.comboBox.addItem('Pepperoni')

        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_8.addWidget(self.comboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(140, 330, 321, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_7.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_7.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_7.addWidget(self.radioButton_3)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(140, 410, 321, 81))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_9.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout_9.addWidget(self.radioButton_5)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(140, 490, 321, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")

        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)

        #Added code
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_4)
        self.comboBox_2.addItem('--None--')
        self.comboBox_2.addItem('Mushrooms')
        self.comboBox_2.addItem('Olives')
        self.comboBox_2.addItem('Extra cheese')
        self.comboBox_2.addItem('Jalapenos')
        
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_10.addWidget(self.comboBox_2)
        
        
        #submitButton
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(510, 550, 75, 23))
        self.submitButton.setObjectName("submitButton")
        self.submitButton.clicked.connect(self.clicked)#Event clicked

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 712, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Pizza choice:"))
        self.label.setText(_translate("MainWindow", "Name : "))
        self.label_3.setText(_translate("MainWindow", "Email: "))
        self.label_2.setText(_translate("MainWindow", "Phone:"))
        self.label_4.setText(_translate("MainWindow", "Age :"))
        self.label_7.setText(_translate("MainWindow", "Name:"))
        self.label_6.setText(_translate("MainWindow", "Size : "))
        self.radioButton.setText(_translate("MainWindow", "small"))
        self.radioButton_2.setText(_translate("MainWindow", "medium"))
        self.radioButton_3.setText(_translate("MainWindow", "large"))
        self.label_8.setText(_translate("MainWindow", "Delivery : "))
        self.radioButton_4.setText(_translate("MainWindow", "True"))
        self.radioButton_5.setText(_translate("MainWindow", "False"))
        self.label_9.setText(_translate("MainWindow", "Toppings"))

        self.submitButton.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow() #Name of class
    ui.setupUi(MainWindow) #setupUi is name of method in ui_Mainwindow class
    #Load data in JSON file at the beginning of the program
    #loadDatainJSONFile()
    
    MainWindow.show()
    sys.exit(app.exec_())
