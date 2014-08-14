import sys
from PySide.QtGui import *


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QAction("Exit", self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menuBar = QMenuBar()
        # 表示されない
        # menu = QMenu("Test")
        # menu.addAction(exitAction)
        # menuBar.addMenu(menu)
        menu = menuBar.addMenu("Test2") # 表示される
        action = menu.addAction("Test3") # 表示され、意図通りに動いた
        action.setShortcut("Ctrl+Q")
        action.setStatusTip('Exit application')
        action.triggered.connect(self.close)
        self.setMenuBar(menuBar)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')


app = QApplication(sys.argv)
window = Example()
window.show()
sys.exit(app.exec_())
