# Routes Overview
This is there all the external facing API routes go.

### Legacy Routes
These support the ability to load sessions from the initial AIThreads implementation. Accessible via ```/legacy/<route>``` , with the following routes:

- ```get_session?&id=<id>``` : return parsed JSON structured according to conversation models.
- ```list_session```: returns list of JSON files (individual AIThreads session) from the top level /data/session_logs/ directory. Useful for debugging, exporation.