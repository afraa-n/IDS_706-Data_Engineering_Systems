"""main module"""
import datetime

def log(message):
    '''
    Log a message along with a timestamp.
    '''
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}"
    return log_message
