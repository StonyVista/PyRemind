# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pyremlegacyui
import pyremsavefunctions
from datetime import datetime


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(400, 300))
        Form.setMaximumSize(QtCore.QSize(400, 300))
        self.btn_createnew = QtWidgets.QPushButton(Form)
        self.btn_createnew.setGeometry(QtCore.QRect(230, 240, 161, 51))
        self.btn_createnew.setObjectName("btn_createnew")
        self.label_welcome = QtWidgets.QLabel(Form)
        self.label_welcome.setGeometry(QtCore.QRect(10, 0, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_welcome.setFont(font)
        self.label_welcome.setLineWidth(1)
        self.label_welcome.setObjectName("label_welcome")
        self.label_todaysreminders = QtWidgets.QLabel(Form)
        self.label_todaysreminders.setGeometry(QtCore.QRect(10, 30, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_todaysreminders.setFont(font)
        self.label_todaysreminders.setLineWidth(1)
        self.label_todaysreminders.setObjectName("label_todaysreminders")
        self.label_todaysreminders_2 = QtWidgets.QLabel(Form)
        self.label_todaysreminders_2.setGeometry(QtCore.QRect(10, 65, 381, 121))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_todaysreminders_2.setFont(font)
        self.label_todaysreminders_2.setLineWidth(1)
        self.label_todaysreminders_2.setObjectName("label_todaysreminders_2")
        self.btn_settings = QtWidgets.QPushButton(Form)
        self.btn_settings.setGeometry(QtCore.QRect(230, 190, 161, 51))
        self.btn_settings.setObjectName("btn_settings")
        self.label_todaysreminders_3 = QtWidgets.QLabel(Form)
        self.label_todaysreminders_3.setGeometry(QtCore.QRect(110, 260, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_todaysreminders_3.setFont(font)
        self.label_todaysreminders_3.setLineWidth(1)
        self.label_todaysreminders_3.setObjectName("label_todaysreminders_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.btn_createnew.clicked.connect(self.createNew)
        self.btn_settings.clicked.connect(self.settingsMenu)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "pyRemind GUI"))
        self.btn_createnew.setText(_translate("Form", "Create a new reminder"))
        self.label_welcome.setText(_translate("Form", "Hello! Welcome to your reminder GUI!"))
        self.label_todaysreminders.setText(_translate("Form", "Today\'s Reminders:"))
        try:
            self.label_todaysreminders_2.setText(_translate("Form", pyremsavefunctions.loadSaveFromDate(datetime.now().strftime('%d/%m/%y'))))
        except:
            self.label_todaysreminders_2.setText(_translate("Form", 'No reminders found'))
        self.btn_settings.setText(_translate("Form", "Settings"))
        self.label_todaysreminders_3.setText(_translate("Form", "Version: "+pyremsavefunctions.getVersionInfo()))

    def createNew(self):
        pyremlegacyui.addevent()
    def settingsMenu(self):
        pyremlegacyui.settingsUI()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
