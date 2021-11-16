import sys

import PyQt5
from functions import encodeData
from PyQt5.QtWidgets import QBoxLayout, QLabel, QLineEdit, QFormLayout, QPushButton, QWidget, QTextBrowser,QComboBox
from PyQt5 import QtGui, QtCore

class Main(QWidget) :
    
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("crc")
        #self.setGeometry(200,200,300, 300)

        validator = QtGui.QRegExpValidator

        self.mainLayout = QFormLayout()

        self.setFixedWidth(1200)
        
        self.inputDropdown()
        self.encodeInputLabel()
        self.encodeInput()
        self.encodeSubmitButton()
        self.decodeInputLabel()
        self.decodeInput()
        self.decodeSubmitButton()
        self.outputDropdown()
        self.encodeOuput()
        self.decodeOuput()
        self.clearButton()
        self.inputValidation()
        self.setLayout(self.mainLayout)
        self.show()
        
    def encodeInput(self):
        self.encodeInput = QLineEdit()
        self.encodeInput.setStyleSheet('font-weight: bold; font-size: 20px; padding:8px; margin:0px 12px 6px 12px; border:0px; ')
        self.encodeInput.setProperty('class', 'danger')
        self.mainLayout.addWidget(self.encodeInput)

    def decodeInput(self):
        self.decodeInput = QLineEdit()
        self.decodeInput.setStyleSheet('font-weight: bold; font-size: 20px; padding:8px; margin:0px 12px 6px 12px; border:0px;')
        self.mainLayout.addWidget(self.decodeInput)
    
    def decodeInputLabel(self):
        self.decodeInputLabel = QLabel('Insert your data to decode')
        self.decodeInputLabel.setStyleSheet('font-weight: bold; font-size: 20px; margin:6px 0px 6px 12px;' )
        self.mainLayout.addWidget(self.decodeInputLabel)

    def encodeInputLabel(self):
        self.encodeInputLabel = QLabel('Insert your data to encode')
        self.encodeInputLabel.setStyleSheet('font-weight: bold; font-size: 20px; margin:6px 0px 6px 12px;')  
        self.mainLayout.addWidget(self.encodeInputLabel)

    def encodeSubmitButton(self):
        self.encodeSubmitButton = QPushButton('Encode')
        self.encodeSubmitButton.setMaximumWidth(200)
        self.encodeSubmitButton.setStyleSheet('margin:6px 12px 24px 12px; font-weight: bold; font-size: 20px;')
        self.encodeSubmitButton.setProperty('class', 'danger')
        self.encodeSubmitButton.clicked.connect(self.encodeButtonClick)
        self.mainLayout.addWidget(self.encodeSubmitButton)

    def decodeSubmitButton(self):
        self.decodeSubmitButton = QPushButton('Decode')
        self.decodeSubmitButton.setMaximumWidth(200)
        self.decodeSubmitButton.setStyleSheet('margin:6px 12px 24px 12px; font-weight: bold; font-size: 20px;')
        self.decodeSubmitButton.clicked.connect(self.decodeButtonClick)
        self.mainLayout.addWidget(self.decodeSubmitButton)

    def clearButton(self):
        self.clearButton = QPushButton('Clear')
        self.clearButton.setMaximumWidth(200)
        self.clearButton.setStyleSheet('margin:6px 12px 24px 12px; font-weight: bold; font-size: 20px;')
        self.clearButton.setProperty('class', 'warning')
        self.clearButton.clicked.connect(self.clearButtonClick)
        self.mainLayout.addWidget(self.clearButton)

    def encodeOuput(self):
        self.encodeOutput = QTextBrowser()
        self.encodeOutput.setText('Encoded data : ')
        self.encodeOutput.setStyleSheet('font-weight: bold; font-size: 20px; margin:6px 0px 6px 12px; border: 0px;')
        self.mainLayout.addWidget(self.encodeOutput)
        

    def decodeOuput(self):
        self.decodeOutput = QTextBrowser()
        self.decodeOutput.setText('Decoded data : ')
        self.decodeOutput.setStyleSheet('font-weight: bold; font-size: 20px; margin:6px 0px 6px 12px; border: 0px;')
        self.mainLayout.addWidget(self.decodeOutput)

    def encodeButtonClick(self):

        if self.inputDropdown.currentText() == 'BIN':
            input = self.encodeInput.text()
        elif self.inputDropdown.currentText() == 'HEX' :
            input = str(bin(int(self.encodeInput.text(), 16))[2:])

        data = encodeData(input,'1001')
        self.encodeOutput.setText('Encoded data : ' + data)
        self.encodeOutput.setProperty('class', 'danger')
        
        
        

    def decodeButtonClick(self):

        if self.inputDropdown.currentText() == 'BIN':
            input = self.encodeInput.text()
        elif self.inputDropdown.currentText() == 'HEX' :
            input = str(bin(int(self.encodeInput.text(), 16))[2:])

        data = encodeData(input,'1001')
        self.decodeOutput.setText('Decoded data : ' + data)


    
    def clearButtonClick(self):
        self.encodeInput.clear()
        self.decodeInput.clear()
        self.decodeOutput.setText('Decoded data : ')
        self.encodeOutput.setText('Encoded data : ')

    
    def inputDropdown(self):
        self.inputDropdownLabel = QLabel('Input data format')
        self.inputDropdownLabel.setStyleSheet('font-weight: bold; font-size: 20px; margin:6px 0px 6px 12px;' )
        self.inputDropdown = QComboBox()
        self.inputDropdown.addItems(['BIN', 'HEX','ASCII'])
        self.inputDropdown.currentIndexChanged.connect(self.inputDropdownChanged)
        self.inputDropdown.setStyleSheet('font-weight: bold; font-size: 20px; margin:6px 0px 6px 12px;') 
        self.inputDropdown.setMaximumWidth(200)
        self.mainLayout.addWidget(self.inputDropdownLabel)
        self.mainLayout.addWidget(self.inputDropdown)
    
    def outputDropdown(self):
        self.outputDropdownLabel = QLabel('Output data format')
        self.outputDropdownLabel.setStyleSheet('font-weight: bold; font-size: 20px; margin:6px 0px 6px 12px;' )
        self.outputDropdown = QComboBox()
        self.outputDropdown.addItems(['BIN', 'HEX'])
        self.outputDropdown.currentIndexChanged.connect(self.outputDropdownChanged)
        self.outputDropdown.setStyleSheet('font-weight: bold; font-size: 20px; margin:6px 0px 6px 12px;') 
        self.outputDropdown.setMaximumWidth(200)
        self.mainLayout.addWidget(self.outputDropdownLabel)
        self.mainLayout.addWidget(self.outputDropdown)

    def inputValidation(self):

        self.binRegex = QtCore.QRegExp('^[0-1]{1,}$')
        self.hexRegex = QtCore.QRegExp('[0-9a-fA-F]{1,}$')
        
        if self.inputDropdown.currentText() == 'BIN':
            self.validator = QtGui.QRegExpValidator(self.binRegex)
        elif self.inputDropdown.currentText() == 'HEX':
            self.validator = QtGui.QRegExpValidator(self.hexRegex)

        self.encodeInput.setValidator(self.validator)
        self.decodeInput.setValidator(self.validator)

    def inputDropdownChanged(self):
        if self.inputDropdown.currentText() == 'BIN':
            self.validator = QtGui.QRegExpValidator(self.binRegex)
        elif self.inputDropdown.currentText() == 'HEX':
             self.validator = QtGui.QRegExpValidator(self.hexRegex)
       
        
        self.encodeInput.clear()
        self.encodeOutput.setText('Encoded data : ')
        self.encodeInput.setValidator(self.validator)

    def outputDropdownChanged(self):

        if self.outputDropdown.currentText() == 'BIN':
            self.validator = QtGui.QRegExpValidator(self.binRegex)
        elif self.outputDropdown.currentText() == 'HEX':
             self.validator = QtGui.QRegExpValidator(self.hexRegex)

        self.decodeOutput.clear()
        self.decodeOutput.setText('Decoded data : ')
        self.decodeInput.setValidator(self.validator)