# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python\QT\pr_4.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pr_4(object):
    def setupUi(self, pr_4):
        pr_4.setObjectName("pr_4")
        pr_4.resize(930, 710)
        self.label = QtWidgets.QLabel(pr_4)
        self.label.setGeometry(QtCore.QRect(0, 0, 931, 711))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\Python\\QT\\image.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(pr_4)
        self.label_2.setGeometry(QtCore.QRect(380, -10, 301, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(pr_4)
        self.label_3.setGeometry(QtCore.QRect(120, 60, 651, 601))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("D:\\Python\\QT\\pr_4.PNG"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(pr_4)
        self.pushButton.setGeometry(QtCore.QRect(670, 660, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(pr_4)
        QtCore.QMetaObject.connectSlotsByName(pr_4)

    def retranslateUi(self, pr_4):
        _translate = QtCore.QCoreApplication.translate
        pr_4.setWindowTitle(_translate("pr_4", "Изучение Питона"))
        self.label_2.setText(_translate("pr_4", "Выражения"))
        self.pushButton.setText(_translate("pr_4", "ОК"))



