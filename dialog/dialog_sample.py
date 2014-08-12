import sys
from PySide.QtGui import *


class Form(QDialog):
    def __init__(self):
        super(Form, self).__init__()
        self.edit = QLineEdit("Write My Name Here")
        self.button = QPushButton("Show Greetings")

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.button.clicked.connect(self.greetings)

    def greetings(self):
        print("Hello {}".format(self.edit.text()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())