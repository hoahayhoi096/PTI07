import os

class Config():
    LOCAL_DIR = os.getcwd()
    UI_DIR = os.path.join(LOCAL_DIR, "ui")

    ANIME_JSON_PATH = 'data/data.json'
    ACCOUNT_JSON_PATH = 'data/account.json'

    HOME_PAGE_INDEX = 0
    RANK_PAGE_INDEX = 1
    USER_PAGE_INDEX = 2
    CRUD_MENU_INDEX= 3
