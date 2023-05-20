import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from menu import Ui_MainWindow
from tem1 import Ui_Form
from zd1 import Ui_zd1
from start import Ui_start
from pr_3_1 import Ui_pr_3_1
from pr_3_2 import Ui_pr_3_2
from pr_3_3 import Ui_pr_3_3
from pr_4 import Ui_pr_4
from zd4 import Ui_zd_4
from pr_2 import Ui_pr_2
from zd_2 import Ui_zd_4 as Ui_zd_2
from zd_3 import Ui_zd3
from pr_5_1 import Ui_pr_2
from pr_5_2 import Ui_pr_2 as Ui_pr_5_2
from pr_5_3 import Ui_pr_2 as Ui_pr_5_3
import random
from zd_5 import Ui_zd_5
from pr_6 import Ui_pr_6
from pr_7 import Ui_pr_7
from pr_8 import Ui_pr_8
from zd_8 import Ui_zd_8
from zd_6 import Ui_zd_6
from zd_7 import Ui_zd_7
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap



app = QtWidgets.QApplication(sys.argv)

pixmap = QPixmap("icon.ico")
app.setWindowIcon(QtGui.QIcon('icon.ico'))




start = QtWidgets.QDialog()
ui = Ui_start()
ui.setupUi(start)
start.setWindowIcon(QtGui.QIcon('icon.ico'))
start.show()


def open_menu():

	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()

	#######################change COLOR
	green_color=("QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(90, 176, 55, 255), stop:0.579545 rgba(248, 115, 114, 255), stop:1 rgba(255, 173, 255, 255));\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 138, 189, 255), stop:0.55 rgba(72, 35, 235, 255), stop:0.98 rgba(218, 6, 6, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}")
	###### Color ZD
	def color_green_1():
		ui.pushButton_9.setStyleSheet(green_color)
	def color_green_2():
		ui.pushButton_10.setStyleSheet(green_color)
	def color_green_3():
		ui.pushButton_11.setStyleSheet(green_color)
	def color_green_4():
		ui.pushButton_12.setStyleSheet(green_color)
	def color_green_5():
		ui.pushButton_13.setStyleSheet(green_color)
	def color_green_6():
		ui.pushButton_14.setStyleSheet(green_color)
	def color_green_7():
		ui.pushButton_15.setStyleSheet(green_color)
	def color_green_8():
		ui.pushButton_16.setStyleSheet(green_color)

	####### Color PR
	def color_green_p1():
		ui.pushButton_3.setStyleSheet(green_color)
	def color_green_p2():
		ui.pushButton_6.setStyleSheet(green_color)
	def color_green_p3():
		ui.pushButton_7.setStyleSheet(green_color)
	def color_green_p4():
		ui.pushButton_5.setStyleSheet(green_color)
	def color_green_p5():
		ui.pushButton_8.setStyleSheet(green_color)
	def color_green_p6():
		ui.pushButton_4.setStyleSheet(green_color)
	def color_green_p7():
		ui.pushButton_2.setStyleSheet(green_color)
	def color_green_p8():
		ui.pushButton.setStyleSheet(green_color)




	#logic open...
	def pr1():
		global Form
		Form = QtWidgets.QWidget()
		ui = Ui_Form()
		ui.setupUi(Form)
		MainWindow.hide()
		Form.show() 


		def retern_main():
			
			Form.close()
			MainWindow.show()
			color_green_p1()
			
			

		ui.ok.clicked.connect(retern_main)
		

	def zd1():
		global zd1
		zd1 = QtWidgets.QWidget()
		ui = Ui_zd1()
		ui.setupUi(zd1)
		MainWindow.hide()
		zd1.show()



		def retern_zd1():
			if ui.label_2.text():
				zd1.close()
				MainWindow.show()
				color_green_1()
			elif ui.label_3.text():
				zd1.close()
				MainWindow.show()
			
			
		ui.ok.clicked.connect(retern_zd1)

		
		

	def pr_3_1():

		global pr_3_1
		pr_3_1 = QtWidgets.QWidget()
		ui = Ui_pr_3_1()
		ui.setupUi(pr_3_1)
		MainWindow.hide()
		pr_3_1.show()

		#2рая страница
		def pr_3_2():

			global pr_3_2
			pr_3_2 = QtWidgets.QWidget()
			ui = Ui_pr_3_2()
			ui.setupUi(pr_3_2)
			pr_3_1.hide()
			pr_3_2.show()


			# 3 страница
			def pr_3_3():
				global pr_3_3
				pr_3_3 = QtWidgets.QWidget()
				ui = Ui_pr_3_3()
				ui.setupUi(pr_3_3)
				pr_3_2.hide()
				pr_3_3.show()

				#main menu
				def exit_pr_3_3():
					pr_3_3.close()
					MainWindow.show()
					color_green_p3()


				ui.pushButton.clicked.connect(exit_pr_3_3)


				#уходим на 2рую страницу
				def retern_pr_3_2_iz_pr_33():
					global pr_3_2
					pr_3_2 = QtWidgets.QWidget()
					ui = Ui_pr_3_2()
					ui.setupUi(pr_3_2)
					pr_3_3.hide()
					pr_3_2.show()

					#уходим из 2рой страницы на первую  
					def ize():
						global pr_3_1
						pr_3_1 = QtWidgets.QWidget()
						ui = Ui_pr_3_1()
						ui.setupUi(pr_3_1)
						pr_3_2.hide()
						pr_3_1.show()
					ui.pushButton_2.clicked.connect(ize)

					#уходим с 2 рой страницы на 3тью
					def back():
						global pr_3_3
						pr_3_3 = QtWidgets.QWidget()
						ui = Ui_pr_3_3()
						ui.setupUi(pr_3_3)
						pr_3_2.hide()
						pr_3_3.show()


						def back33():
							pr_3_3.close()
							MainWindow.show()
							color_green_p3()


						ui.pushButton.clicked.connect(back33)

					ui.pushButton.clicked.connect(back)


				ui.pushButton_2.clicked.connect(retern_pr_3_2_iz_pr_33)


				#уходим на 1 страницу
			def pr_3_1_retern():
				global pr_3_1
				pr_3_1 = QtWidgets.QWidget()
				ui = Ui_pr_3_1()
				ui.setupUi(pr_3_1)
				pr_3_2.hide()
				pr_3_1.show()
				#возвращаемся на 2рую страницу
				def retern_pr_3_2():
					global pr_3_2
					pr_3_2 = QtWidgets.QWidget()
					ui = Ui_pr_3_2()
					ui.setupUi(pr_3_2)
					pr_3_1.hide()
					pr_3_2.show()

					def next3_3():
						global pr_3_3
						pr_3_3 = QtWidgets.QWidget()
						ui = Ui_pr_3_3()
						ui.setupUi(pr_3_3)
						pr_3_2.hide()
						pr_3_3.show()

						def back33():
							pr_3_3.close()
							MainWindow.show()
							color_green_p3()

						ui.pushButton.clicked.connect(back33)

					ui.pushButton.clicked.connect(next3_3)


				ui.pushButton.clicked.connect(retern_pr_3_2)

			ui.pushButton_2.clicked.connect(pr_3_1_retern)
			ui.pushButton.clicked.connect(pr_3_3)

		ui.pushButton.clicked.connect(pr_3_2)

	def pr_4():
		global pr_4
		pr_4 = QtWidgets.QWidget()
		ui = Ui_pr_4()
		ui.setupUi(pr_4)
		MainWindow.hide()
		pr_4.show()
		def ret():
			pr_4.hide()
			MainWindow.show()
			color_green_p4()
		ui.pushButton.clicked.connect(ret)

	def pr_2():

		pr_2 = QtWidgets.QWidget()
		ui = Ui_pr_2()
		ui.setupUi(pr_2)
		MainWindow.hide()
		pr_2.show()
		def back():
			pr_2.close()
			MainWindow.show()
			color_green_p2()
		ui.pushButton_2.clicked.connect(back)


	def zd4():
		zd_4 = QtWidgets.QWidget()
		ui = Ui_zd_4()
		ui.setupUi(zd_4)
		MainWindow.hide()
		zd_4.show()
		def retrn():
			if ui.label_9.text():
				zd_4.close()
				MainWindow.show()
				color_green_4()
			elif ui.label_10.text():
				zd_4.close()
				MainWindow.show()

		ui.pushButton_2.clicked.connect(retrn)

	def zd2():

		zd_2 = QtWidgets.QWidget()
		ui = Ui_zd_2()
		ui.setupUi(zd_2)
		MainWindow.hide()
		zd_2.show()
		def exit():
			if ui.label_9.text():
				zd_2.close()
				MainWindow.show()
				color_green_2()
			elif ui.label_10.text():
				zd_2.close()
				MainWindow.show()


		ui.pushButton_2.clicked.connect(exit)
  

	def zd3():

		zd3 = QtWidgets.QWidget()
		ui = Ui_zd3()
		ui.setupUi(zd3)
		MainWindow.hide()
		zd3.show()
		def ex():
			if ui.label_2.text():
				zd3.close()
				MainWindow.show()
				color_green_3()
			elif ui.label_3.text():
				zd3.close()
				MainWindow.show()
				
		ui.pushButton_2.clicked.connect(ex)


	def pr_5():

		pr_2 = QtWidgets.QWidget()
		ui = Ui_pr_2()
		ui.setupUi(pr_2)
		MainWindow.hide()
		pr_2.show()

		##PR_5_2
		def pr_5_2():

			pr_5_2 = QtWidgets.QWidget()
			ui = Ui_pr_5_2()
			ui.setupUi(pr_5_2)
			pr_2.hide()
			pr_5_2.show()
		
			def pr_5_3():

				pr_5_3 = QtWidgets.QWidget()
				ui = Ui_pr_5_3()
				ui.setupUi(pr_5_3)
				pr_5_2.hide()
				pr_5_3.show()


				def retern_main():
					pr_5_3.close()
					MainWindow.show()
					color_green_p5()
				ui.pushButton_2.clicked.connect(retern_main)
			ui.pushButton_2.clicked.connect(pr_5_3)
		ui.pushButton_2.clicked.connect(pr_5_2)






		def ret_main():
			pr_2.close()
			MainWindow.show()
		ui.pushButton_3.clicked.connect(ret_main)

	def zd5():

		zd_5 = QtWidgets.QWidget()
		ui = Ui_zd_5()
		ui.setupUi(zd_5)
		MainWindow.hide()
		zd_5.show()
		def ex():
			if ui.label_5.text():
				zd_5.close()
				MainWindow.show()
				color_green_5()
			elif ui.label_7.text():
				zd_5.close()
				MainWindow.show()
		ui.pushButton_3.clicked.connect(ex)
	   
	def pr_6():
		pr_6 = QtWidgets.QWidget()
		ui = Ui_pr_6()
		ui.setupUi(pr_6)
		MainWindow.hide()
		pr_6.show()
		def ex():
			pr_6.close()
			MainWindow.show()
			color_green_p6()
		ui.pushButton_2.clicked.connect(ex)
	

	def pr_7():
		pr_7 = QtWidgets.QWidget()
		ui = Ui_pr_7()
		ui.setupUi(pr_7)
		MainWindow.hide()
		pr_7.show()
		def exx():
			pr_7.close()
			MainWindow.show()
			color_green_p7()
		ui.pushButton_2.clicked.connect(exx)


	def pr_8():
		pr_8 = QtWidgets.QWidget()
		ui = Ui_pr_8()
		ui.setupUi(pr_8)
		MainWindow.hide()
		pr_8.show()
		def exit():
			pr_8.close()
			MainWindow.show()
			color_green_p8()
		ui.pushButton_2.clicked.connect(exit)



	def zd8():

		zd_8 = QtWidgets.QWidget()
		ui = Ui_zd_8()
		ui.setupUi(zd_8)
		MainWindow.hide()
		zd_8.show()
		def execs():
			try:
				if ui.label_5.text():
					zd_8.close()
					MainWindow.show()
					color_green_8()
				elif ui.label_7.text():
					zd_8.close()
					MainWindow.show()
			except RuntimeError:
				zd_8.close()
				MainWindow.show()
		ui.pushButton_2.clicked.connect(execs)

	def zd6():

		zd_6 = QtWidgets.QWidget()
		ui = Ui_zd_6()
		ui.setupUi(zd_6)
		MainWindow.hide()
		zd_6.show()
		def nexts():
			try:
				if ui.label_5.text():
					zd_6.close()
					MainWindow.show()
					color_green_6()
				elif ui.label_7.text():
					zd_6.close()
					MainWindow.show()
			except RuntimeError:
				zd_6.close()
				MainWindow.show()
			
		ui.pushButton_3.clicked.connect(nexts)

	def zd7():

		zd_7 = QtWidgets.QWidget()
		ui = Ui_zd_7()
		ui.setupUi(zd_7)
		MainWindow.hide()
		zd_7.show()


		def nextse():
			try:
				if ui.label_5.text():
					zd_7.close()
					MainWindow.show()
					color_green_7()
				elif ui.label_7.text():
					zd_7.close()
					MainWindow.show()
			except RuntimeError:
				zd_7.close()
				MainWindow.show()

		ui.pushButton_3.clicked.connect(nextse)
	#logic...

	#open PR
	ui.pushButton_3.clicked.connect(pr1)
	ui.pushButton_7.clicked.connect(pr_3_1)
	ui.pushButton_5.clicked.connect(pr_4)
	ui.pushButton_6.clicked.connect(pr_2)
	ui.pushButton_8.clicked.connect(pr_5)
	ui.pushButton_4.clicked.connect(pr_6)
	ui.pushButton_2.clicked.connect(pr_7)
	ui.pushButton.clicked.connect(pr_8)

	#open ZD
	ui.pushButton_9.clicked.connect(zd1)
	ui.pushButton_12.clicked.connect(zd4)
	ui.pushButton_10.clicked.connect(zd2)
	ui.pushButton_11.clicked.connect(zd3)
	ui.pushButton_13.clicked.connect(zd5)
	ui.pushButton_14.clicked.connect(zd6)
	ui.pushButton_15.clicked.connect(zd7)
	ui.pushButton_16.clicked.connect(zd8)

	


ui.buttonBox.clicked.connect(open_menu)

sys.exit(app.exec_())