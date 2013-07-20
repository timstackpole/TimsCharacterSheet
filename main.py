#!/usr/bin/env python

# Getting the QT libraries.
from PyQt4 import QtCore, QtGui
import os

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
		# Make the whole window a text box
		self.text = QtGui.QTextEdit(self)
		# Show the text box
		self.setCentralWidget(self.text)

	# File Menu
	def createFileMenu(self):
		#
		# The Quit option in the File Menu
		#
		# The first option of a quit button is easy
		exitOption = QtGui.QAction('&Exit', self)
		# Allow for keyboard shortcut
		exitOption.setShortcut('Ctrl+Q')
		# The status shows up at the bottom of the window title
		exitOption.setStatusTip('Exit application')
		# Connect the button with a quit
		exitOption.triggered.connect(self.close)
		#
		# The Save option in the File Menu
		#
		saveOption = QtGui.QAction('&Save', self)
		# Allow for keyboard shortcut
		saveOption.setShortcut('Ctrl+S')
		# The status shows up at the bottom of the window title
		saveOption.setStatusTip('Save the file.')
		# Connect the button with a quit
		saveOption.triggered.connect(self.saveFile)
		
		#
		# The Open option in the File Menu
		#
		openOption = QtGui.QAction('&Open', self)
		# Allow for keyboard shortcut
		openOption.setShortcut('Ctrl+O')
		# The status shows up at the bottom of the window title
		openOption.setStatusTip('Open a file.')
		# Connect the button with a quit
		openOption.triggered.connect(self.openFile)
		
		#
		# Making the statusBar appear on the bottom of the window
		#
		self.statusBar()

		#
		# Creating the menu bar
		#
		menubar = self.menuBar()
		# Giving a title to the file menu
		fileMenu = menubar.addMenu('&File')
		# Add the open option to the menu
		fileMenu.addAction(openOption)
		# Add the save option to the menu
		fileMenu.addAction(saveOption)
		# Add the exit option to the menu
		fileMenu.addAction(exitOption)

	# Saving a file
	def saveFile(self):
		# Start the user off in their home directory
		filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
		# Open the file context for writing
		f = open(filename, 'w')
		# Save it out as plain text
		filedata = self.text.toPlainText()
		# Close the write stream
		f.write(filedata)
		# Close the file
		f.close()
	
	# Opening a file; almost cutNpaste from save with tweaks
	def openFile(self):
		# Start the user off in their home directory
		filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
		# Open the file context for writing
		f = open(filename, 'r')
		# Read in the text
		filedata = f.read()
		# Set the text
		self.text.setText(filedata)
		# Close the file
		f.close()

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
