from PyQt6.QtWidgets import QMainWindow, QListWidgetItem, QMessageBox, QListView, QAbstractItemView
from PyQt6 import uic 
import os
from config import Config
from PyQt6.QtCore import Qt, QSize
from script.DialogScr import AddDialog , EditDialog
from script.AnimeItemScr import AnimeItemWidget


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

        self.pushButtonAdd.clicked.connect(self.onPushButtonAdd)
        self.pushButtonEdit.clicked.connect(self.onPushButtonEdit)
        self.pushButtonDelete.clicked.connect(self.onPushButtonDelete)

        self.setup_rank_page()
        
        self.pushButtonTopAnime.clicked.connect(self.onPushButtonTopAnime)
        self.pushButtonLastest.clicked.connect(self.onPushButtonLastest)
        self.pushButtonAtoZ.clicked.connect(self.onPushButtonAtoZ)

        self.pushButtonSearch_2.clicked.connect(self.onPushButtonSearch_2)
        self.pushButtonSearch.clicked.connect(self.onPushButtonSearch)




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

    def onPushButtonAdd(self):
        # Lấy chỉ số của dòng hiện tại trong listWidgetAnime
        currIndex = self.listWidgetAnime.currentRow()
        # Tạo hộp thoại Add dialog
        add_dialog = AddDialog()

        # Hiển thị hộp thoại và thêm dữ liệu mới khi người dùng nhấn ok
        if add_dialog.exec():
            # Lấy dữ liệu từ hộp thoại dưới dạng một dictionary
            inputs = add_dialog.return_input_fields()

            # Thêm mục mới vào danh sách listWidgetAnime tại vị trí currIndex
            self.listWidgetAnime.insertItem(currIndex, inputs["title"])

            # Lưu dữ liệu mới vào cơ sở dữ liệu
            self.database.add_item_from_dict(inputs)

            self.setup_rank_page()

    def onPushButtonEdit(self):
        # Lấy phần tử trong listWidgetAnime
        current_item = self.listWidgetAnime.currentItem()

        if current_item:
            # Lấy id của bộ anime từ UserRole
            anime_id = current_item.data(Qt.ItemDataRole.UserRole)

            # Lấy bộ anime bằng id 
            edit_item = self.database.get_item_by_id(anime_id)
            # Khởi tạo hộp thoại EditDialog 
            edit_dialog = EditDialog(edit_item)
            # Mở hộp thoại lên & kiểm tra nếu có dữ liệu được tra về thì thực hành động ...
            if edit_dialog.exec():
                # Lấy các trường dữ liệu có trong hộp thoại ra 
                inputs = edit_dialog.return_input_fields()
                # Cập nhập lại tiêu đề anime trong listWidget
                current_item.setText(inputs["title"])
                # Cập nhật lại dữ liệu trong file json
                self.database.edit_item_from_dict(anime_id, inputs)

                self.setup_rank_page()

    def onPushButtonDelete(self):
        # Lấy chỉ số của item hiện tại trong listWidget 
        curr_index = self.listWidgetAnime.currentRow()
        # Kiểm tra item đã được chọn hay chưa 
        if curr_index == -1:
            QMessageBox.warning(self, "Error", "Bạn chưa chọn anime để xoá!")
            return
        
        # Lấy anime hiện tại đang được chọn 
        item = self.listWidgetAnime.item(curr_index)
        item_title = item.text()

        # Lấy id của bộ anime vừa chọn thông qua User role 
        anime_id = item.data(Qt.ItemDataRole.UserRole)

        # Hiển thị hộp thoại xác nhận 
        question = QMessageBox.question(
            self, 
            "Remove Anime", 
            f"Bạn có muốn xoá bộ anime '{item_title}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if question == QMessageBox.StandardButton.Yes:
            # Xoá đi item khỏi listWidget 
            self.listWidgetAnime.takeItem(curr_index)

            # Gọi hàm xoá anime từ khỏi database
            self.database.delete_item(anime_id)

            QMessageBox.information(self, "Success", "Bạn đã xoá anime: " + item_title )
            self.setup_rank_page()

    def setup_rank_page(self):

        # Xoá hết dữ liệu cũ/rác trong listwidget 
        # Đặt khoảng cách giữa các widget con trong listWidget 
        self.listWidgetAnimeRanking.clear()
        self.listWidgetAnimeRanking.setSpacing(10)

        # Đặt chế độ hiển thị item theo chiều ngang 
        self.listWidgetAnimeRanking.setFlow(QListView.Flow.LeftToRight)

        # Bật thanh cuộng ngang (chỉ cần áp dụng)
        self.listWidgetAnimeRanking.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.listWidgetAnimeRanking.setWrapping(False)  # Không cho phép wrap item xuống dòng

        # Load các widget chứa thông tin các bộ anime lên listWidget
        anime_list = self.database.anime_list

        for anime in anime_list:
            animeWidget = AnimeItemWidget(anime)
            # Tạo đối tượng con của listWidgetAnimeRanking
            item = QListWidgetItem(self.listWidgetAnimeRanking)

            # Lưu lại id của bộ anime trong user role 
            item.setData(Qt.ItemDataRole.UserRole, anime.id)
            # Đặt kích thước cố định cho animeWidget
            animeWidget.setFixedSize(250, 500)
            # Đặt kích thước cho phần tử con của listWidgetAnimeRanking
            item.setSizeHint(QSize(250, 500))
            
            self.listWidgetAnimeRanking.addItem(item)
            # Kết hợp item và animeWidget để thêm vào listWidgetAnimeRanking
            self.listWidgetAnimeRanking.setItemWidget(item, animeWidget)

    def onPushButtonTopAnime(self):
        self.database.sort_item_by_rating()
        self.setup_rank_page()

    def onPushButtonLastest(self):
        self.database.sort_item_by_date()
        self.setup_rank_page()

    def onPushButtonAtoZ(self):
        self.database.sort_item_by_title()
        self.setup_rank_page()

    def onPushButtonSearch_2(self):
        # Lấy từ khoá từ lineEditSearch_2
        keyword = self.lineEditSearch_2.text().strip()

        # Kiểm tra từ khoá có rỗng hay không
        if keyword:
            for i in range(self.listWidgetAnime.count()):
                item = self.listWidgetAnime.item(i)
                # Kiểm tra từ khoá có trong tiêu đề của item hay không
                if keyword.lower() in item.text().lower():
                    # Hiển thị item đó lên listWidget
                    item.setHidden(False)
                else:
                    item.setHidden(True)
        else:
            # Hiển thị tất cả item
            for i in range(self.listWidgetAnime.count()):
                item = self.listWidgetAnime.item(i)
                item.setHidden(False)

    def onPushButtonSearch(self):
        # Lấy từ khoá từ lineEditSearch
        keyword = self.lineEditSearch.text().strip()

        # Mở trang ranking
        self.stackedWidget.setCurrentIndex(2)

        # Kiểm tra từ khoá có rỗng hay không
        if keyword:
            for i in range(self.listWidgetAnimeRanking.count()):
                item = self.listWidgetAnimeRanking.item(i)
                # Lấy widget con của item
                animeWidget = self.listWidgetAnimeRanking.itemWidget(item)
                if animeWidget:
                    # Kiểm tra từ khoá có trong tiêu đề của item hay không
                    animeTitle = animeWidget.anime.title.lower()
                    if keyword.lower() in animeTitle:
                        # Hiển thị item đó lên listWidget
                        item.setHidden(False)
                    else:
                        item.setHidden(True)
        else:
            # Hiển thị tất cả item
            for i in range(self.listWidgetAnimeRanking.count()):
                item = self.listWidgetAnimeRanking.item(i)
                item.setHidden(False)