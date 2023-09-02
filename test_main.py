"""test_main module"""
import main

def log_testing():
    '''
    testing function for log
    '''
    assert not main.log("This is a log message.").isEmpty()
