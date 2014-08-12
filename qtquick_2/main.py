import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *


class MainWindow(QDeclarativeView):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Main Window")
        self.setSource(QUrl("view.qml"))
        self.setResizeMode(QDeclarativeView.SizeRootObjectToView)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
