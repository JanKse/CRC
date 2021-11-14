import sys
from PyQt5.QtWidgets import QLabel, QLineEdit, QFormLayout, QPushButton, QWidget

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
        encodeInput = QLineEdit()
        encodeInput.setStyleSheet('font-weight: bold; font-size: 20px; padding:8px; margin:0px 12px 6px 12px;')
        self.mainLayout.addWidget(encodeInput)

    def decodeInput(self):
        decodeInput = QLineEdit()
        decodeInput.setStyleSheet('font-weight: bold; font-size: 20px; padding:8px; margin:0px 12px 6px 12px;')
        self.mainLayout.addWidget(decodeInput)
    
    def decodeInputLabel(self):
        decodeInputLabel = QLabel('Insert your data to decode')
        decodeInputLabel.setStyleSheet('font-weight: bold; font-size: 20px; margin:6px 0px 6px 12px;')
        self.mainLayout.addWidget(decodeInputLabel)

    def encodeInputLabel(self):
        encodeInputLabel = QLabel('Insert your data to encode')
        encodeInputLabel.setStyleSheet('font-weight: bold; font-size: 20px; margin:6px 0px 6px 12px;')  
        self.mainLayout.addWidget(encodeInputLabel)

    def encodeSubmitButton(self):
        encodeSubmitButton = QPushButton('Encode')
        encodeSubmitButton.setMaximumWidth(200)
        encodeSubmitButton.setStyleSheet('margin:6px 12px 24px 12px; font-weight: bold; font-size: 20px;')
        self.mainLayout.addWidget(encodeSubmitButton)

    def decodeSubmitButton(self):
        decodeSubmitButton = QPushButton('Decode')
        decodeSubmitButton.setMaximumWidth(200)
        decodeSubmitButton.setStyleSheet('margin:6px 12px 24px 12px; font-weight: bold; font-size: 20px;')
        self.mainLayout.addWidget(decodeSubmitButton)