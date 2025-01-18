import uuid 
class Account:
    def __init__(self, email, password):
        self.id = str(uuid.uuid4())
        self.email = email
        self.password = password
