import sys
from PyQt5.QtWidgets import QApplication, QWidget
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget() #base class of all objects
    w.resize(300,300) ##resize window
    w.setWindowTitle("Guru99") # change title of window
    w.show() # displays widget
    sys.exit(app.exec_()) # closes only when user closes from GUI
    
    