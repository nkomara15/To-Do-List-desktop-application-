from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(456, 461)
        self.AddItem = QtWidgets.QPushButton(parent=Dialog, clicked = lambda: self.add_it())
        self.AddItem.setGeometry(QtCore.QRect(30, 80, 101, 31))
        self.AddItem.setObjectName("AddItem")
        self.DeleteItem = QtWidgets.QPushButton(parent=Dialog, clicked = lambda: self.delete_it())
        self.DeleteItem.setGeometry(QtCore.QRect(140, 80, 131, 31))
        self.DeleteItem.setObjectName("DeleteItem")
        self.Clearall = QtWidgets.QPushButton(parent=Dialog, clicked = lambda: self.clear_it())
        self.Clearall.setGeometry(QtCore.QRect(280, 80, 111, 31))
        self.Clearall.setObjectName("Clearall")
        self.Additem_lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.Additem_lineEdit.setGeometry(QtCore.QRect(30, 40, 361, 41))
        self.Additem_lineEdit.setObjectName("Additem_lineEdit")
        self.mylist_listWidget = QtWidgets.QListWidget(parent=Dialog)
        self.mylist_listWidget.setGeometry(QtCore.QRect(30, 120, 361, 201))
        self.mylist_listWidget.setObjectName("mylist_listWidget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # Add item to list
    def add_it(self):
        # grab item from list box
        item = self.Additem_lineEdit.text()
        # add item to list 
        self.mylist_listWidget.addItem(item)
        #clear the item box to add next item
        self.Additem_lineEdit.setText("")

    #delete item from list
    def delete_it(self):
        # grab the item 
        clicked = self.mylist_listWidget.currentRow()
        # only delete if an item is selected
        if clicked >= 0:
            self.mylist_listWidget.takeItem(clicked)
    
    
    # Clear all from list 
    def clear_it(self):
        self.mylist_listWidget.clear()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "To-Do list"))
        self.AddItem.setText(_translate("Dialog", "Add Item to list"))
        self.DeleteItem.setText(_translate("Dialog", "Delete Item from list"))
        self.Clearall.setText(_translate("Dialog", "Clear list"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())


