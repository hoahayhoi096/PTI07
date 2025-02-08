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

    def add_item_from_dict(self, anime_dict):
        new_item = Anime(title=anime_dict["title"],
                             release_date=anime_dict["release_date"],
                             image=anime_dict["image"],
                             rating=anime_dict["rating"],
                             link=anime_dict["link"])
        self.anime_list.append(new_item)
        self.anime_dict_data.append(anime_dict)
        write_anime_json_data(self.anime_dict_data)


def date_to_text(date:datetime):
    return date.strftime("%b %Y")

def format_date(date_text):
    return datetime.strptime(date_text, '%b %Y')