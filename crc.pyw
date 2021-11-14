import sys
from PyQt5 import QtWidgets 
from GUI.Main import Main
from qt_material import apply_stylesheet
from GUI.TextInput import TextInput
import functions



if __name__ == '__main__' :
    
    app = QtWidgets.QApplication([])
    apply_stylesheet(app, theme='dark_teal.xml')
    main = Main()
    #textInput = TextInput()
    
    
    
    app.exec_()








