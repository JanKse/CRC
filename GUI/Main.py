import sys
from functions import encodeData
from PyQt5.QtWidgets import QLabel, QLineEdit, QFormLayout, QPushButton, QWidget
import PyQt5.QtCore

class Main(QWidget) :
    
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("crc")
        #self.setGeometry(200,200,300, 300)
        self.mainLayout = QFormLayout()
        self.encodeInputLabel()
        self.encodeInput()
        self.encodeSubmitButton()
        
        self.decodeInputLabel()
        self.decodeInput()
        self.decodeSubmitButton()
        self.setLayout(self.mainLayout)
        self.show()
        
    def encodeInput(self):
        self.encodeInput = QLineEdit()
        self.encodeInput.setStyleSheet('font-weight: bold; font-size: 20px; padding:8px; margin:0px 12px 6px 12px;')
        self.mainLayout.addWidget(self.encodeInput)

    def decodeInput(self):
        self.decodeInput = QLineEdit()
        self.decodeInput.setStyleSheet('font-weight: bold; font-size: 20px; padding:8px; margin:0px 12px 6px 12px;')
        self.mainLayout.addWidget(self.decodeInput)
    
    def decodeInputLabel(self):
        self.decodeInputLabel = QLabel('Insert your data to decode')
        self.decodeInputLabel.setStyleSheet('font-weight: bold; font-size: 20px; margin:6px 0px 6px 12px;')
        self.mainLayout.addWidget(self.decodeInputLabel)

    def encodeInputLabel(self):
        self.encodeInputLabel = QLabel('Insert your data to encode')
        self.encodeInputLabel.setStyleSheet('font-weight: bold; font-size: 20px; margin:6px 0px 6px 12px;')  
        self.mainLayout.addWidget(self.encodeInputLabel)

    def encodeSubmitButton(self):
        self.encodeSubmitButton = QPushButton('Encode')
        self.encodeSubmitButton.setMaximumWidth(200)
        self.encodeSubmitButton.setStyleSheet('margin:6px 12px 24px 12px; font-weight: bold; font-size: 20px;')
        self.encodeSubmitButton.clicked.connect(self.buttonClick)
        self.mainLayout.addWidget(self.encodeSubmitButton)

    def decodeSubmitButton(self):
        self.decodeSubmitButton = QPushButton('Decode')
        self.decodeSubmitButton.setMaximumWidth(200)
        self.decodeSubmitButton.setStyleSheet('margin:6px 12px 24px 12px; font-weight: bold; font-size: 20px;')
        self.mainLayout.addWidget(self.decodeSubmitButton)

    def buttonClick(self):
        data = self.encodeInput.text()
        data = encodeData(self.encodeInput.text(),'1001')
        print(data)