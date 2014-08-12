import sys
from PySide.QtCore import *
from PySide.QtGui import *
from ui_editor import Ui_reSTEditor
from docutils.core import publish_string


class EditorWindow(QMainWindow):
    def __init__(self):
        super(EditorWindow, self).__init__()
        self.ui = Ui_reSTEditor()
        self.ui.setupUi(self)
        self.ui.convert.clicked.connect(self.converted)

    def converted(self):
        text = self.ui.plainTextEdit.toPlainText()
        try:
            html = publish_string(text, writer_name="html").decode("utf-8")
        except:
            pass
        self.ui.webView.setHtml(html)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditorWindow()
    window.show()
    sys.exit(app.exec_())
