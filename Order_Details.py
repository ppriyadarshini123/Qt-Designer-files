# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Order_Details.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import json


class Ui_Dialog(object):

    def loaddata(self):
        with open('./Qt Designer files/test.json', 'r') as file: # Open the file for reading and writing. Read this: https://www.geeksforgeeks.org/how-to-open-and-close-a-file-in-python/
            # In the relative path, it will look for a file into the directory where this script is running.
            #First we load existing data into a dict.
            file_data = json.load(file)
            print(len(file_data["orders"]))
            self.tableWidget.setRowCount(len(file_data["orders"]))
            row = 0
            for order in file_data["orders"]: 
                #Check if order is not empty               
                if len(order["order"]) != 0:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(order["order"]["pizza"]))  
                    #Set column width of each column
                    self.tableWidget.setColumnWidth(0,120) 
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(order["order"]["size"]))  
                    #Set column width of each column
                    self.tableWidget.setColumnWidth(1,50) 
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(order["order"]["delivery"]))  
                    #Set column width of each column
                    self.tableWidget.setColumnWidth(2,50) 
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(order["order"]["toppings"]))  
                    #Set column width of each column
                    self.tableWidget.setColumnWidth(3,100) 
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(order["order"]["client"]))  
                    #Set column width of each column
                    self.tableWidget.setColumnWidth(4,100) 
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(order["order"]["email"]))  
                    #Set column width of each column
                    self.tableWidget.setColumnWidth(5,100) 
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(order["order"]["phone"]))  
                    #Set column width of each column
                    self.tableWidget.setColumnWidth(6,100) 
                    self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(order["order"]["age"]))  
                    #Set column width of each column
                    self.tableWidget.setColumnWidth(7,100) 
                    

                    #updateButton
                    self.updateButton = QtWidgets.QPushButton(self.tableWidget)
                    self.updateButton.setGeometry(QtCore.QRect(510, 550, 75, 23))
                    self.updateButton.setText('Update')
                    self.updateButton.setObjectName("updateButton")
                    self.updateButton.clicked.connect(self.updateclicked)#Event clicked

                    #Add a button to the cell
                    self.tableWidget.setCellWidget(row, 8, self.updateButton)  
                    #Set column width of each column
                    self.tableWidget.setColumnWidth(8,100) 

                    #deleteButton
                    self.deleteButton = QtWidgets.QPushButton(self.tableWidget)
                    self.deleteButton.setGeometry(QtCore.QRect(510, 550, 75, 23))
                    self.deleteButton.setText('Delete')
                    self.deleteButton.setObjectName("deleteButton")
                    
                    self.tableWidget.selectionModel().selectionChanged.connect(self.deleteclicked)#Event clicked

                    #Add a button to the cell
                    self.tableWidget.setCellWidget(row, 9, self.deleteButton)  
                    #Set column width of each column
                    self.tableWidget.setColumnWidth(9,100) 

                row+=1
        #Good practice to close the file after use.
        file.close()


    def updateclicked(self):
        pass

    def deleteclicked(self, selected):
        # if int(self.tableWidget.rowCount()) > 0:
        #     self.tableWidget.removeRow(self.tableWidget.rowCount()-1)        
        with open('./Qt Designer files/test.json', 'r+') as file: # Open the file for reading and writing. Read this: https://www.geeksforgeeks.org/how-to-open-and-close-a-file-in-python/
            # In the relative path, it will look for a file into the directory where this script is running.
            #First we load existing data into a dict.
            file_data = json.load(file)
            #print(len(file_data["orders"]))
            self.tableWidget.setRowCount(len(file_data["orders"]))
            row = 0

            for order in file_data["orders"]:
                if len(order["order"]["client"]) != 0:
                    if order["order"]["client"] == self.tableWidget.item(self.tableWidget.currentRow(), 4).text():
                        del order["order"]["pizza"]
                        del order["order"]["size"]
                        del order["order"]["delivery"]
                        del order["order"]["toppings"]
                        del order["order"]["client"]
                        del order["order"]["email"]
                        del order["order"]["phone"]
                        del order["order"]["age"]
                        json.dump(file_data, file, indent=4)
        #Write updated data
        with open('./Qt Designer files/test.json', 'w') as file:
            json.dump(file_data, file, indent=4)  
        file.close()  
                    
                    
        


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1284, 601)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(560, 530, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(40, 40, 1211, 461))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)

        #load data from dictionary
        self.loaddata()


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Pizza name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Size"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Delivery"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Topping"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Customer name"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Email"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Phone"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Age"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "Update"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())