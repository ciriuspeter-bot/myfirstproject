import sys
from PyQt6.QtWidgets import *

class Button(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Color select")
        self.setGeometry(300, 300, 600, 400)
        self.btn_1 = QPushButton("Red", self)
        self.btn_1.move(30, 30)        
        self.btn_1.setStyleSheet("background-color: red")
        self.btn_2 = QPushButton("Blue", self)
        self.btn_2.move(30, 60)
        self.btn_2.setStyleSheet("background-color: blue")
        self.btn_3 = QPushButton("Green", self)
        self.btn_3.move(30, 90)
        self.btn_3.setStyleSheet("background-color: green")
        self.btn_group = QButtonGroup(self)
        self.btn_group.addButton(self.btn_1, 0)
        self.btn_group.addButton(self.btn_2, 1)
        self.btn_group.addButton(self.btn_3, 2)
        self.btn_group.idClicked[int].connect(self.on_Click)
        self.show()
    def on_Click(self, id):
        if id == 0:
            self.setStyleSheet("background-color: red")
        if id == 1:
            self.setStyleSheet("background-color: blue")
        if id == 2:
            self.setStyleSheet("background-color: green")
       
app = QApplication(sys.argv)
Color = Button()
sys.exit(app.exec())

