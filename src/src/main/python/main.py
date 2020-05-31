from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys
from main_gui import Ui_MainWindow

class DijkstraGui(QMainWindow, Ui_MainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		
		# event
		self.btnGenerate.clicked.connect(self.btnGenerate_Clicked)
		self.btnFind.clicked.connect(self.btnFind_Clicked)
		self.cbxShowSteps.stateChanged.connect(self.cbxShowSteps_Clicked)
		self.lineEditPoint.textChanged.connect(self.lineEditPoint_TextChanged)
		self.lineEditLine.textChanged.connect(self.lineEditLine_TextChanged)

		self.countPoints = self.lineEditPoint.text()
		self.countLines = self.lineEditLine.text()

	def btnGenerate_Clicked(self):
		print("btnGenerate")
		print("Point: {0}".format(self.countPoints))
		print("Line: {0}".format(self.countLines))
		
	def btnFind_Clicked(self):
		print("btnFind")

	def cbxShowSteps_Clicked(self, int):
		if (self.cbxShowSteps.isChecked()):
			print("cbxShowSteps Checked")
		else:
			print("cbxShowSteps unChecked")
	
	def lineEditPoint_TextChanged(self):
		self.countPoints = self.lineEditPoint.text()

	def lineEditLine_TextChanged(self):
		self.countLines = self.lineEditLine.text()
		
def main():
	appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
	window = DijkstraGui()
	window.show()
	exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
	sys.exit(exit_code)

if __name__ == '__main__':
	main()