import sys
from PyQt5 import QtWidgets
import functions



if __name__ == '__main__' :
    
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    win.setGeometry(200,200,300, 300)
    win.setWindowTitle("ahoooj")
    label = QtWidgets.QLabel(win)
    label.setText("My faaa")
    label.move(50,50)
    win.show()
    sys.exit(app.exec_())








