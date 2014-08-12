import sys
from PySide.QtGui import *

app = QApplication(sys.argv)

window = QWidget()
window.resize(200, 200)
window.setWindowTitle("Title")

quit = QPushButton("Quit", window)
quit.setFont(QFont("Times", 18, QFont.Bold))
quit.setGeometry(10, 40, 180, 40)
quit.clicked.connect(app.quit)

window.show()

sys.exit(app.exec_())