from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QLabel
import Ui_untitled as myform
from PyQt5 import uic

def button_clicked():
    print("Button clicked")

if __name__ == "__main__":
    app = QApplication([])

    window = QMainWindow()
    uic.loadUi("untitled.ui", window)
    button = window.findChild(QPushButton, 'pushButton')
    if button:
        button.clicked.connect(button_clicked)
    lable = window.findChild(QLabel, 'label')
    if lable:
        lable.setText("HelloWorld")
    window.show()

    app.exec_()