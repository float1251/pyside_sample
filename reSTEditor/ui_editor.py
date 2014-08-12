# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created: Tue Aug 12 21:37:28 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_reSTEditor(object):
    def setupUi(self, reSTEditor):
        reSTEditor.setObjectName("reSTEditor")
        reSTEditor.resize(855, 609)
        self.centralwidget = QtGui.QWidget(reSTEditor)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 9, 2, 2))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.convert = QtGui.QPushButton(self.centralwidget)
        self.convert.setGeometry(QtCore.QRect(350, 550, 111, 32))
        self.convert.setAutoRepeat(False)
        self.convert.setObjectName("convert")
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(3, 7, 401, 531))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(410, 10, 20, 531))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(430, 0, 381, 531))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        reSTEditor.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(reSTEditor)
        self.statusbar.setObjectName("statusbar")
        reSTEditor.setStatusBar(self.statusbar)

        self.retranslateUi(reSTEditor)
        QtCore.QMetaObject.connectSlotsByName(reSTEditor)

    def retranslateUi(self, reSTEditor):
        reSTEditor.setWindowTitle(QtGui.QApplication.translate("reSTEditor", "reSTEditor", None, QtGui.QApplication.UnicodeUTF8))
        self.convert.setText(QtGui.QApplication.translate("reSTEditor", "変換", None, QtGui.QApplication.UnicodeUTF8))

from PySide import QtWebKit
