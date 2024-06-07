import uuid

class Chat:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages

    def get_id(self):
        return self.id
