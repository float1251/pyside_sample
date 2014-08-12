# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sample.ui'
#
# Created: Tue Aug 12 11:32:53 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_JsonFormatterDialog(object):
    def setupUi(self, JsonFormatterDialog):
        JsonFormatterDialog.setObjectName("JsonFormatterDialog")
        JsonFormatterDialog.resize(400, 305)
        self.buttonBox = QtGui.QDialogButtonBox(JsonFormatterDialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 260, 401, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayoutWidget = QtGui.QWidget(JsonFormatterDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 391, 241))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.InputJsonEdit = QtGui.QPlainTextEdit(self.horizontalLayoutWidget)
        self.InputJsonEdit.setObjectName("InputJsonEdit")
        self.horizontalLayout.addWidget(self.InputJsonEdit)

        self.retranslateUi(JsonFormatterDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), JsonFormatterDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(JsonFormatterDialog)

    def retranslateUi(self, JsonFormatterDialog):
        JsonFormatterDialog.setWindowTitle(QtGui.QApplication.translate("JsonFormatterDialog", "JSON Formatter", None, QtGui.QApplication.UnicodeUTF8))

