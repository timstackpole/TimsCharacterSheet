#!/usr/bin/env python

# Getting the QT libraries.
from PyQt4 import QtCore, QtGui

# Our primary class where the magic happens
class TimCharacterSheet(QtGui.QMainWindow):
	# Defining the class for the main program
	def __init__(self):
		# Initialize the class and make it the top window.
		super(TimCharacterSheet, self).__init__()
		# Set the window title
		self.setWindowTitle("Tim's Character Sheet")
		# Create the "File" menu
		self.createFileMenu()
		# Set the initial size of the application
		self.resize(1024, 768)
	# File Menu
	def createFileMenu(self):
		# The first option of a quit button is easy
		exitOption = QtGui.QAction('&Exit', self)
		# Allow for keyboard shortcut
		exitOption.setShortcut('Ctrl+Q')
		# The status shows up at the bottom of the window title
		exitOption.setStatusTip('Exit application')
		# Connect the button with a quit
		exitOption.triggered.connect(QtGui.qApp.quit)
		# Making the statusBar appear on the bottom of the window
		self.statusBar()
		# Creating the menu bar
		menubar = self.menuBar()
		# Giving a title to the file menu
		fileMenu = menubar.addMenu('&File')
		# Displaying the file menu
		fileMenu.addAction(exitOption)


# Our main class. Basically this only runs if the python script is called
# directly.
if __name__ == '__main__':
	# The sys module gives us access to the arguments that might be passed in 
	# from the command line.
	import sys
	# Create the QApplication object; every PyQT app has to have this.
	app = QtGui.QApplication(sys.argv)
	# Create a object and put the class created above into it.
	tcs = TimCharacterSheet()
	# Create and display the window.
	tcs.show()
	# Exit when the window is closed.
	sys.exit(app.exec_())
