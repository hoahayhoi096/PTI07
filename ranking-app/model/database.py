from model.account import Account
from data.data_io import load_account_json_data, write_account_json_data

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