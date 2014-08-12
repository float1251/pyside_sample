import sys, json
from PySide import QtGui
from sample import Ui_JsonFormatterDialog


class JsonFormatterDialog(QtGui.QWidget):
    def __init__(self):
        super(JsonFormatterDialog, self).__init__()
        self.ui = Ui_JsonFormatterDialog()
        self.ui.setupUi(self)

    def accept(self):
        print(self.ui.InputJsonEdit.toPlainText())
        text = self.ui.InputJsonEdit.toPlainText()
        try:
            text = json.dumps(json.loads(text), sort_keys=True, indent=4)
        except Exception as e:
            error = QtGui.QErrorMessage()
            error.setWindowTitle("Convert Error")
            error.showMessage(str(e))
            error.exec_()
        print(text)
        self.ui.InputJsonEdit.setPlainText(text)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dialog = JsonFormatterDialog()
    dialog.show()
    sys.exit(app.exec_())
