from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic 
import os
from config import Config


class MainPage(QMainWindow):  
    def __init__(self, controller):
        super().__init__()

        # Tải các thành phần giao diện 
        ui_path = os.path.join(os.path.dirname(__file__), "../UI/MainPage.ui")
        uic.loadUi(ui_path, self)

        self.controller = controller
        # self.database = database

        self.pushButtonAccount.clicked.connect(self.onPushButtonAccount)
        self.pushButtonHome.clicked.connect(self.onPushButtonHome)


    def onPushButtonHome(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def onPushButtonAccount(self):
        self.stackedWidget.setCurrentIndex(0)


