import sys
from PySide.QtWebKit import *
from PySide.QtGui import *


if __name__ == "__main__":
    app = QApplication(sys.argv)
    webView = QWebView()
    webView.load("http://google.co.jp")
    webView.show()
    sys.exit(app.exec_())