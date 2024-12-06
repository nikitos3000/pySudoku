from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
import sys

qapp = QApplication(sys.argv)

def on_button_click():
    label.setText("КТ-7")



win = QWidget()

win.setWindowTitle("R7b")
win.setGeometry(100, 100, 2000, 1000)


label = QLabel("hi", parent=win)
label.setGeometry(50,50,200,30)

button = QPushButton("СК-1",parent=win)
button.setGeometry(50,100,100,30)
button.clicked.connect(on_button_click)


win.show()

qapp.exec_()