# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python\QT\pr_5_3.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pr_2(object):
    def setupUi(self, pr_2):
        pr_2.setObjectName("pr_2")
        pr_2.resize(880, 648)
        self.label = QtWidgets.QLabel(pr_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 881, 651))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\Python\\QT\\image.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(pr_2)
        self.label_2.setGeometry(QtCore.QRect(290, -30, 351, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(pr_2)
        self.pushButton_2.setGeometry(QtCore.QRect(740, 560, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(pr_2)
        self.pushButton_3.setGeometry(QtCore.QRect(-10, 560, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(pr_2)
        self.label_3.setGeometry(QtCore.QRect(130, 40, 611, 521))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("D:\\Python\\QT\\5 тема(3).PNG"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(pr_2)
        QtCore.QMetaObject.connectSlotsByName(pr_2)

    def retranslateUi(self, pr_2):
        _translate = QtCore.QCoreApplication.translate
        pr_2.setWindowTitle(_translate("pr_2", "Изучение Питона"))
        self.label_2.setText(_translate("pr_2", "Цикл for и оператор while"))
        self.pushButton_2.setText(_translate("pr_2", "Выход"))


