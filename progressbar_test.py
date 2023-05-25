# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_progressbar.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(666, 428)
        Dialog.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.pressMeButton = QtWidgets.QPushButton(Dialog)
        self.pressMeButton.setGeometry(QtCore.QRect(140, 250, 93, 28))
        self.pressMeButton.setStyleSheet("background-color: rgb(130, 135, 139);\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"PMingLiU\";")
        self.pressMeButton.setObjectName("pressMeButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(80, 180, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 130, 130, 20))
        self.label.setStyleSheet("font: 12pt \"PMingLiU\";\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.helloButton = QtWidgets.QPushButton(Dialog)
        self.helloButton.setGeometry(QtCore.QRect(140, 300, 93, 28))
        self.helloButton.setStyleSheet("background-color: rgb(130, 135, 139);\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"PMingLiU\";")
        self.helloButton.setObjectName("helloButton")
        self.pic = QtWidgets.QLabel(Dialog)
        self.pic.setGeometry(QtCore.QRect(330, 50, 300, 300))
        self.pic.setText("")
        self.pic.setPixmap(QtGui.QPixmap("Lenna.jpg"))
        self.pic.setAlignment(QtCore.Qt.AlignCenter)
        self.pic.setObjectName("pic")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(40, 40, 98, 19))
        self.radioButton.setAutoExclusive(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(40, 70, 98, 19))
        self.radioButton_2.setAutoExclusive(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(200, 50, 80, 22))
        self.comboBox.setObjectName("comboBox")
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(220, 380, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(30, 370, 141, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "你好"))
        self.pressMeButton.setText(_translate("Dialog", "press me"))
        self.label.setText(_translate("Dialog", "please enter value"))
        self.helloButton.setText(_translate("Dialog", "show string"))
        self.radioButton.setText(_translate("Dialog", "RadioButton"))
        self.radioButton_2.setText(_translate("Dialog", "RadioButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())