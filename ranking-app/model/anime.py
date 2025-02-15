import uuid 
class Anime:
    def __init__(self, title, release_date, image = None, rating = None , link = None):
        self.id = str(uuid.uuid4())
        self.title = title
        self.release_date = release_date
        self.image = image
        self.rating = float(rating)
        self.link = link

    def update(self, new_data):
        # Chỉ cập nhật những trường dữ liệu được thay đổi
        for key, value in new_data.items():
            if value:
                setattr(self, key, value)

    
