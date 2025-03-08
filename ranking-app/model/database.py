import operator
from model.account import Account
from model.anime import Anime
from data.data_io import load_account_json_data, write_account_json_data, load_anime_json_data, write_anime_json_data
from datetime import datetime

class AccountDatabase:
    def __init__(self):
        self.account_list = list()
        self.account_dict_data = load_account_json_data()
        
    def load_data(self): # Lấp đầy dữ liệu cho self.account_list
        for account_dict in self.account_dict_data:
            account = Account(email = account_dict["email"],
                              password = account_dict["password"])
            self.account_list.append(account)

    def add_item_from_dict(self, account_dict):
        new_item = Account(email = account_dict["email"],
                           password = account_dict["password"])
        self.account_list.append(new_item)
        self.account_dict_data.append(account_dict)
        write_account_json_data(self.account_dict_data)


class AnimeDatabase:
    def __init__(self):
        self.anime_list = list()
        self.anime_dict_data = load_anime_json_data()

    def load_data(self): # Lấp đầy dữ liệu cho self.anime_list
        for anime_dict in self.anime_dict_data:
            anime = Anime(title = anime_dict["title"],
                              release_date= anime_dict["release_date"],
                              image=anime_dict["image"],
                              rating=anime_dict["rating"])
            self.anime_list.append(anime)

    # chuyển object python sang json
    def item_to_data(self):
        json_data = list()
        for anime in self.anime_list:
            json_data.append(anime.__dict__)
        return json_data 
    
    def add_item_from_dict(self, anime_dict):
        new_item = Anime(title=anime_dict["title"],
                             release_date=anime_dict["release_date"],
                             image=anime_dict["image"],
                             rating=anime_dict["rating"],
                             link=anime_dict["link"])
        self.anime_list.append(new_item)
        self.anime_dict_data.append(anime_dict)
        write_anime_json_data(self.anime_dict_data)

    def get_item_by_id(self, anime_id) -> Anime:
        for anime in self.anime_list:
            if anime.id == anime_id:
                return anime
            
    def edit_item_from_dict(self, edit_id, anime_edit: Anime):
        anime = self.get_item_by_id(edit_id)
        # Gọi hàm update từ file anime.py để cập nhật lại dữ liệu mới
        anime.update(anime_edit)
        # Chuyển dữ liệu python sang json
        self.anime_dict_data = self.item_to_data()
        # Viết dữ liệu mới vào json
        write_anime_json_data(self.anime_dict_data) 

    def delete_item(self, item_id):
        # Lấy ra bộ anime cần xoá bằng id
        anime_delete = self.get_item_by_id(item_id)
        # Xoá bộ anime khỏi ds python 
        self.anime_list.remove(anime_delete)
        # Lấy ds json mới nhất từ ds đối tượng python
        self.anime_dict_data = self.item_to_data()
        # Viết dữ liệu json mới nhất vào file .json
        write_anime_json_data(self.anime_dict_data)

    def sort_item_by_rating(self):
        self.anime_list = sorted(self.anime_list, 
                                 key=operator.attrgetter('rating'),
                                 reverse = True)

    def sort_item_by_title(self):
        pass
    def sort_item_by_date(self):
        pass

def date_to_text(date:datetime):
    return date.strftime("%b %Y")

def format_date(date_text):
    return datetime.strptime(date_text, '%b %Y')