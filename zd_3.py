# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python\QT\zd3.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_zd3(object):
    def setupUi(self, zd3):
        zd3.setObjectName("zd3")
        zd3.resize(843, 597)
        self.fon_start = QtWidgets.QLabel(zd3)
        self.fon_start.setGeometry(QtCore.QRect(-50, -10, 891, 621))
        self.fon_start.setText("")
        self.fon_start.setPixmap(QtGui.QPixmap("D:\\Python\\QT\\image.jpg"))
        self.fon_start.setScaledContents(True)
        self.fon_start.setObjectName("fon_start")
        self.label = QtWidgets.QLabel(zd3)
        self.label.setGeometry(QtCore.QRect(160, -10, 691, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(zd3)
        self.lineEdit.setGeometry(QtCore.QRect(140, 160, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(zd3)
        self.pushButton.setGeometry(QtCore.QRect(270, 230, 231, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(zd3)
        self.label_2.setGeometry(QtCore.QRect(300, 320, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(111, 255, 89);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(zd3)
        self.label_3.setGeometry(QtCore.QRect(290, 450, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 21, 24);\n"
"background-color: rgb(100, 96, 92);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(zd3)
        self.label_4.setGeometry(QtCore.QRect(270, 70, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(zd3)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 510, 231, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(zd3)
        self.label_5.setGeometry(QtCore.QRect(240, 360, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(111, 255, 89);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(zd3)
        self.label_6.setGeometry(QtCore.QRect(240, 410, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(111, 255, 89);")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(zd3)
        QtCore.QMetaObject.connectSlotsByName(zd3)

    def retranslateUi(self, zd3):
        _translate = QtCore.QCoreApplication.translate
        zd3.setWindowTitle(_translate("zd3", "Изучение Питона"))
        self.label.setText(_translate("zd3", "Напишите любое математическое действие коректно "))
        self.pushButton.setText(_translate("zd3", "Проверить!"))
        
        
        self.label_4.setText(_translate("zd3", "что бы в окне вышел ответ"))
        self.pushButton_2.setText(_translate("zd3", "Выход"))
        
        

        def ed():
            global g
            g=self.lineEdit.text()
            
            try:
                self.label_5.setText(_translate("zd3",f"Ваш запрос: {g}"))
                res= eval(g)
                self.label_2.setText(_translate("zd3", "Все верно!"))
                self.label_6.setText(_translate("zd3", f"Ответ: {res}"))
                try:
                    self.label_3.deleteLater()
                except RuntimeError:
                    pass
            except NameError:
                 self.label_3.setText(_translate("zd3", "Подумай ещё!"))
            except SyntaxError:
                self.label_3.setText(_translate("zd3", "Подумай ещё!"))

        self.pushButton.clicked.connect(ed)