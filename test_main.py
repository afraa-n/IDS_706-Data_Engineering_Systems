"""test_main module"""
import main

def log_testing():
    '''
    testing function for log
    '''
    assert len(main.log("This is a log message.")) != 0
