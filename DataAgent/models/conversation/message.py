import uuid
import datetime


class Message:
    def __init__(self, content, role, message_type, tags, timestamp=None, thread_id=None,msg_order=0,in_thread=False):
        self.id = str(uuid.uuid4())
        self.content = content
        self.role = role
        self.message_type = message_type
        self.tags = tags
        self.thread_id = thread_id
        self.msg_order = msg_order
        self.in_thread = in_thread
        self.timestamp = timestamp or datetime.datetime.now()

    def get_id(self):
        return self.id

    def get_content(self):
        return self.content

    def get_role(self):
        return self.role

    def get_message_type(self):
        return self.message_type

    def get_tags(self):
        return self.tags
    
    def get_timestamp(self):
        return self.timestamp
    
    def get_thread_id(self):
        return self.thread_id
    
    def get_msg_order(self):
        return self.msg_order
    
    def get_in_thread(self):
        return self.in_thread
    
    def to_json(self):
        return {
            'id': self.id,
            'content': self.content.to_json() if self.content else None,
            'role': self.role,
            'message_type': self.message_type,
            'tags': self.tags,
            'thread_id': self.thread_id,
            'msg_order': self.msg_order,
            'in_thread': self.in_thread,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None
            }
    
    
