from script.LoginScr import Login
from script.MainPageScr import MainPage
# from model.database import AnimeDatabase


class Controller: 
    def __init__(self):
        # Khởi tạo dữ liệu 
        # self.db = AnimeDatabase()

        #Khởi tạo tác cửa sổ 
        self.main_window = MainPage(self)
        self.login_window = Login(self)

    def show_main_page(self):
        self.main_window.show()

    def show_login_page(self):
        self.login_window.show()