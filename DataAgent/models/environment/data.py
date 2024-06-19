import uuid
from flask import current_app

class Data:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.name = ""
        self.location = ""