import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "b'yh\xd1\xab\xe4\x06C\xb41%\xcb^\x8bj\x8bD'"


    MONGODB_SETTINGS ={ 'db':'UTA_Enrollment'}
    
    