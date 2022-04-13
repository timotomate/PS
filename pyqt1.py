import sys
from PyQt5.QtWidgets import * #PyQt5라는 디렉터리의 QtWidgets파일에 있는 모든 것을 import

app = QApplication(sys.argv)
label = QLabel("Hello PyQt")
label.show()
app.exec_()