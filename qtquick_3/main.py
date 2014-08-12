import sys
from PySide.QtGui import *
from PySide.QtDeclarative import *
from PySide.QtCore import *

class MainWindow(QDeclarativeView):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Test")
        self.setSource(QUrl("view.qml"))
        self.setResizeMode(QDeclarativeView.SizeRootObjectToView)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())