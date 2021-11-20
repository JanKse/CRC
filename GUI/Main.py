import sys


from functions import encodeData, decodeData, cyclepoly

from PyQt5.QtWidgets import QBoxLayout, QLabel, QLineEdit, QFormLayout, QPushButton, QWidget, QTextBrowser,QComboBox
from PyQt5 import QtGui, QtCore

class Main(QWidget) :
    
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("crc")
        #self.setGeometry(200,200,300, 300)

        

        self.mainLayout = QFormLayout()

        self.setFixedWidth(1200)
        
    
        self.codeInputLabel()
        self.codeInput()
        self.generateCRCButton()
        self.codeComboBoxLabel()
        self.codeComboBox()
        self.encodeInputLabel()
        self.encodeInput()
        self.encodeSubmitButton()
        self.decodeInputLabel()
        self.decodeInput()
        self.decodeSubmitButton()
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
        
    def codeInput(self):
        self.codeInput = QLineEdit()
        self.codeInput.setStyleSheet('font-weight: bold; font-size: 20px; padding:8px; margin:0px 12px 6px 12px; border:0px;')
        self.mainLayout.addWidget(self.codeInput)


    def decodeInputLabel(self):
        self.decodeInputLabel = QLabel('Insert your data to decode')
        self.decodeInputLabel.setStyleSheet('font-weight: bold; font-size: 20px; margin:6px 0px 6px 12px;' )
        self.mainLayout.addWidget(self.decodeInputLabel)

    def encodeInputLabel(self):
        self.encodeInputLabel = QLabel('Insert your data to encode')
        self.encodeInputLabel.setStyleSheet('font-weight: bold; font-size: 20px; margin:6px 0px 6px 12px;')  
        self.mainLayout.addWidget(self.encodeInputLabel)

    def codeInputLabel(self):
        self.codeInputLabel = QLabel('Insert your code n,k ')
        self.codeInputLabel.setStyleSheet('font-weight: bold; font-size: 20px; margin:6px 0px 6px 12px;')  
        self.mainLayout.addWidget(self.codeInputLabel)
    
    def codeComboBoxLabel(self):
        self.codeComboBoxLabel = QLabel('Choose your code')
        self.codeComboBoxLabel.setStyleSheet('font-weight: bold; font-size: 20px; margin:6px 0px 6px 12px;')  
        self.mainLayout.addWidget(self.codeComboBoxLabel)
    
    def codeComboBox(self):
        self.codeComboBox = QComboBox()
        self.codeComboBox.setStyleSheet('font-weight: bold; font-size: 20px; margin:6px 0px 24px 12px;')  
        self.mainLayout.addWidget(self.codeComboBox)

    def encodeSubmitButton(self):
        self.encodeSubmitButton = QPushButton('Encode')
        self.encodeSubmitButton.setMaximumWidth(200)
        self.encodeSubmitButton.setStyleSheet('margin:6px 12px 24px 12px; font-weight: bold; font-size: 20px;')
        self.encodeSubmitButton.setProperty('class', 'danger')
        self.encodeSubmitButton.clicked.connect(self.encodeButtonClick)
        self.mainLayout.addWidget(self.encodeSubmitButton)
    
    def generateCRCButton(self):
        self.generateCRCButton = QPushButton('Generate gen. pol.')
        self.generateCRCButton.setMaximumWidth(400)
        self.generateCRCButton.setStyleSheet('margin:6px 12px 0px 12px; font-weight: bold; font-size: 20px;')
        self.generateCRCButton.setProperty('class', 'danger')
        self.generateCRCButton.clicked.connect(self.generateCRCButtonClick)
        self.mainLayout.addWidget(self.generateCRCButton)


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

        key = self.codeComboBox.currentText()
        if self.encodeInput.text() != '' :
            input = self.encodeInput.text()
            self.encodedData = encodeData(input,key)
            self.encodeOutput.setText('Encoded data : ' + self.encodedData)
            self.encodeOutput.setProperty('class', 'danger')
        else:
            self.encodeOutput.setText('Encoded data : ')
        
        
    def decodeButtonClick(self):

        key = self.codeComboBox.currentText()
        if self.decodeInput.text() != '' :
            input = self.decodeInput.text()
            self.decodedData = decodeData(input,key)
            if int(self.decodedData[0], 2) == 0:
                self.decodeOutput.setText('Decoded data : ' + self.decodedData[1] + '\nNo error detection')
            else:
                self.decodeOutput.setText('Decoded data : ' + self.decodedData[1] + '\nError detection' + '\nRemainder : ' + self.decodedData[0])
        else:
            self.encodeOutput.setText('Encoded data : ')

    
    def clearButtonClick(self):
        self.codeInput.clear()
        self.codeComboBox.clear()
        self.encodeInput.clear()
        self.decodeInput.clear()
        self.encodeOutput.setText('Encoded data : ')
        self.decodeOutput.setText('Decoded data : ')


    
    def generateCRCButtonClick(self):
        codes = []
        if self.codeInput.text() != '' :
            self.codeComboBox.clear()
            param = self.codeInput.text().split(',')
            codes = cyclepoly(int(param[0]), int(param[1]))
            self.codeComboBox.addItems(codes)
        else:
            self.codeComboBox.clear()
        

    def inputValidation(self):

        self.codeRegex = QtCore.QRegExp('^\d+(,\d+)*$')
        self.binRegex = QtCore.QRegExp('^[0-1]{1,}$')
        self.validator = QtGui.QRegExpValidator(self.binRegex)
        self.codeValidator = QtGui.QRegExpValidator(self.codeRegex)

        self.codeInput.setValidator(self.codeValidator)
        self.encodeInput.setValidator(self.validator)
        self.decodeInput.setValidator(self.validator)

    
    
        