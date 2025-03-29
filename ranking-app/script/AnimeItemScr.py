import os
import webbrowser
from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget

from config import Config

from model.anime import Anime


class AnimeItemWidget(QWidget):
    UI_LOCATION = os.path.join(Config.UI_DIR, "anime_column.ui")
    def __init__(self, anime:Anime):
        QWidget.__init__(self)

        self.ui = uic.loadUi(self.UI_LOCATION, self)

        self.anime = anime
        self.display_description()

        # Thông báo khi hover vào 
        if self.anime.link != 'None':
            self.ui.animeCol.setToolTip("Double click to watch")

        self.ui.animeCol.mouseDoubleClickEvent = lambda x: self.open_link(self.anime.link)
        

    def display_description(self):
        description_text = self.anime.release_date + "\n" \
                            + "Rating: " + str(self.anime.rating) + "/10"
        
        img_pixmap = QPixmap(self.anime.image)
        self.ui.animeView.setPixmap(img_pixmap)
        self.ui.animeTitle.setText(self.anime.title)
        self.ui.animeInfo.setText(description_text)

    def open_link(self, url):
        print(url)
        if url != 'None':
            webbrowser.open(str(url))