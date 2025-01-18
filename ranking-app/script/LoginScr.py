from PyQt6.QtWidgets import QMainWindow, QMessageBox
import sys
from PyQt6 import uic 
import os

from model.database import AccountDatabase

class Login(QMainWindow):  
    def __init__(self, controller):
        super().__init__()

        # Tải các thành phần giao diện 
        ui_path = os.path.join(os.path.dirname(__file__), "../UI/Login.ui")
        uic.loadUi(ui_path, self)

        self.controller = controller

        self.database = AccountDatabase()
        self.setup_login()

        self.pushButtonDangNhap.clicked.connect(self.onPushButtonDangNhapClicked)

    def onPushButtonDangNhapClicked(self):
        taiKhoan = self.lineEditTaiKhoan.text()
        matKhau = self.lineEditMatKhau.text()

        isAuth = False 
        for item in self.database.account_list:
            if item.email == taiKhoan and item.password == matKhau:
                isAuth = True
                break
        
        if isAuth == True:
            self.controller.show_main_page()
            self.close()
        else:
            QMessageBox.information(self, "Đây là thông báo!", "Đăng nhập thất bại, Vui lòng đăng nhập lại!")
        
        
    def setup_login(self):
        self.database.load_data()


    

    
        
