import os
import json
import uuid

from ...models.conversation.message import Message
from ...models.conversation.message_content import MessageContent

from ...config import Config
def create_message(message,thread_id = None,msg_order=0,in_thread=False):
    '''
        Parses the initial version of the AI Threads JSON files
    '''
    tmp = Message(
            #organizing the content into a content object
            content = MessageContent(
                        text=message['content'],
                        image=message['image'] if 'image' in message else None,
                        tags=['one', 'two','three'],
                        caption = message['caption'] if 'caption' in message else None
                    ),
                           
            # remainer of the message information
            in_thread=in_thread,
            role=message['role'],
            message_type = message['type'],
            tags=[],
            thread_id= thread_id,
            msg_order=msg_order
        )
    
    return tmp


def process_message(message,thread_id= None,msg_order=0,in_thread=False):
    try:
        #message appears to have replies
        #replies = message['replies']['history'][0][0]
        replies = message['replies']['history']
        
        if len(replies)>1:
            print("I am in the thread")
            #there are threads
            if thread_id is None:
                thread_id = uuid.uuid4()  # Generate a unique thread ID using UUID

            #process the current message
            msg = create_message(message,thread_id,msg_order,in_thread=False)
            thread = [msg]

            #process the message replies
            reply_order = 1
            for reply in replies:
                thread.append(process_message(reply[0],thread_id,reply_order,in_thread=True))
                reply_order+=1

            #return the result
            return(thread)
        else:
            #just process the current message:
            msgObj = create_message(message[0],thread_id,msg_order,in_thread)
            return(msgObj)

    except:
        #message has no replies
        msgObj = create_message(message,thread_id,msg_order,in_thread)
        return(msgObj)

def parse_session_logs(session_id):
    session_logs_path = Config.SESSION_LOG_DIR
    sessions = []
     
    # Ensure the directory exists
    if not os.path.exists(session_logs_path):
        print(f"Directory {session_logs_path} does not exist.")
        return sessions
    
    else:
        session_file_path = os.path.join(session_logs_path, f"{session_id}.json")
        try:
            with open(session_file_path, 'r') as file:
                session_data = json.load(file)  
                
            msg_order=0

            for message_data in session_data['history']:
                msg = process_message(message_data[0],None, msg_order)
                msg_order +=1
                if type(msg) == list:
                    sessions+=msg
                else:
                    sessions.append(msg)
            #return a list of sessions
            return (sessions)
                
        except FileNotFoundError:
            print(f"No log file found for session ID {session_id}.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the log file for session ID {session_id}.")

