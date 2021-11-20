
from PyQt5 import QtWidgets 
from GUI.Main import Main
from qt_material import apply_stylesheet
from functions import *



if __name__ == '__main__' :
    
    
    
    app = QtWidgets.QApplication([])
    apply_stylesheet(app, theme='dark_teal.xml')
    main = Main()
    #textInput = TextInput()
    
    app.exec_()








