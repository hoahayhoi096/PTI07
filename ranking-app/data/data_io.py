import json
from config import Config

def load_anime_json_data():
    # Khởi tạo một danh sách rỗng:
    anime_dict_data = list()

    # Mở file JSON trong chế độ đọc ("r"):
    with open(Config.ANIME_JSON_PATH, "r") as json_in:
        # Đọc dữ liệu JSON từ file:
        json_data = json.load(json_in)
    # Thêm dữ liệu vừa đọc vào danh sách anime_dict_data:
    anime_dict_data.extend(json_data)
    return anime_dict_data


def load_account_json_data():
    # Khởi tạo một danh sách rỗng:
    account_dict_data = list()
    
    # Mở file JSON trong chế độ đọc ("r"):
    with open(Config.ACCOUNT_JSON_PATH, "r") as json_in:
        # Đọc dữ liệu JSON từ file:
        json_data = json.load(json_in)

    # Thêm dữ liệu vừa đọc vào danh sách account_dict_data:
    account_dict_data.extend(json_data)

    # Trả về danh sách chứa dữ liệu:
    return account_dict_data

def write_account_json_data(json_data):
    # Mở file JSON trong chế độ ghi ("w"):
    with open(Config.ACCOUNT_JSON_PATH, "w") as json_out:
        # Ghi dữ liệu vào file JSON:
        # Chuyển đổi dữ liệu Python (json_data) thành định dạng JSON và ghi vào file json_out.
        json.dump(json_data, json_out)