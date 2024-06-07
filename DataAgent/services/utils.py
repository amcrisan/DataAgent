import json
from datetime import datetime
from uuid import UUID


from ..models.conversation.message import Message
from ..models.conversation.message_content import MessageContent

class CustomEncoder(json.JSONEncoder):
    '''
    Custom JSON encoders for messages and their contents
    '''
    def default(self, obj):
        if isinstance(obj, Message) or isinstance(obj, MessageContent):
            return obj.to_json()  # Ensure MessageContent has a to_json() method
        elif isinstance(obj, datetime):
            # Format datetime object to ISO 8601 string (YYYY-MM-DDTHH:MM:SS)
            return obj.isoformat()
        elif isinstance(obj, UUID):
            # Convert UUID to string
            return str(obj)
           
        # Extend this to handle other custom types as needed
        return json.JSONEncoder.default(self, obj)

def json_encode(data):
    return json.dumps(data, cls=CustomEncoder)