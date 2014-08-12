import sys
from PySide.QtGui import *


app = QApplication(sys.argv)
hello = QPushButton("Hello World")
hello.resize(200, 200)
hello.show()
sys.exit(app.exec_())