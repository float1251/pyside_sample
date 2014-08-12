import sys
from PySide.QtGui import *

app = QApplication(sys.argv)

quit = QPushButton("Quit")
quit.resize(75, 75)
quit.setWindowTitle("Quit Button")
quit.clicked.connect(app.quit)
quit.show()

sys.exit(app.exec_())
