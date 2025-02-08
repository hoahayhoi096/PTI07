from PyQt6.QtWidgets import QMainWindow, QListWidgetItem
from PyQt6 import uic 
import os
from config import Config
from PyQt6.QtCore import Qt


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

        self.setup_manager_page()


    def onPushButtonManager(self):
        self.stackedWidget.setCurrentIndex(3)


    def onPushButtonAnime(self):
        self.stackedWidget.setCurrentIndex(2)

    def onPushButtonHome(self):
        self.stackedWidget.setCurrentIndex(1)

    def onPushButtonAccount(self):
        self.stackedWidget.setCurrentIndex(0)

    def setup_manager_page(self):
        #Lấp đầy dữ liệu cho list anime
        self.database.load_data()

        # Xoá đi dữ liệu có từ trước trong list widget
        self.listWidgetAnime.clear()

        #Thêm dữ liệu vào list widget
        for item in self.database.anime_list:
            # Tạo phần tử con của listWidget
            listWidgetItem = QListWidgetItem(item.title)
            # Gán mã id của anime vào UserRole(lưu trữ tạm dữ liệu)
            listWidgetItem.setData(Qt.ItemDataRole.UserRole, item.id)
            # Thêm item vào listWidget
            self.listWidgetAnime.addItem(listWidgetItem)

        self.listWidgetAnime.setCurrentRow(0)




