import sys

from PyQt5 import uic
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

main_form = uic.loadUiType(r'web_view.ui')[0]

class web_view(QMainWindow, main_form):
    def __init__(self, page="https://rest-time.tistory.com/"):
        super().__init__()
        self.setupUi(self)
        self.webEngineView = QWebEngineView()
        self.page = page
        self.load_page()
        self.verticalLayout_page.addWidget(self.webEngineView)
        self.pushButton_refresh.clicked.connect(self.load_page)

    def set_page(self, page):
        self.page = page

    def load_page(self):
        try:
            print("loading page {}".format(self.page))
            if self.page.startswith("http") == False:
                self.page = f"http://{self.page}"
            self.webEngineView.load(QUrl(self.page))
            return True
        except:
            print("failed to load page")
            return False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = web_view()
    myWindow.set_page("https://rest-time.tistory.com/")
    myWindow.show()
    app.exec_()