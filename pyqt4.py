import sys
from PyQt5.QtWidgets import *
#from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 300)

        btn1 = QPushButton("Click me", self)
        btn1.move(100, 150)#위치 조정
        btn1.clicked.connect(self.btn1_clicked)#버튼 클릭하면 btn1_clicked 이벤트 실행

    def btn1_clicked(self):#btn1_clicked 이벤트 메서드
        QMessageBox.about(self, "message", "clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()