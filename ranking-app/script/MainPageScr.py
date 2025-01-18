from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic 
import os
from config import Config


class MainPage(QMainWindow):  
    def __init__(self, controller, database):
        super().__init__()

        # Tải các thành phần giao diện 
        ui_path = os.path.join(os.path.dirname(__file__), "../UI/MainPage.ui")
        uic.loadUi(ui_path, self)

        self.controller = controller
        self.database = database

        self.pushButtonAccount.clicked.connect(self.onPushButtonAccount)
        self.pushButtonHome.clicked.connect(self.onPushButtonHome)
        self.pushButtonAnime.clicked.connect(self.onPushButtonAnime)
        self.pushButtonManager.clicked.connect(self.onPushButtonManager)

    def onPushButtonManager(self):
        self.stackedWidget.setCurrentIndex(3)


    def onPushButtonAnime(self):
        self.stackedWidget.setCurrentIndex(2)
        # lấp đầy list_anime trong database
        self.database.load_data()
        # Duyệt qua các bộ anime và in ra màn terminal để kiểm tra
        ds_anime = self.database.anime_list
        for anime in ds_anime:
            print("Anime: ", anime.title, "-" , anime.release_date)

    def onPushButtonHome(self):
        self.stackedWidget.setCurrentIndex(1)

    def onPushButtonAccount(self):
        self.stackedWidget.setCurrentIndex(0)


