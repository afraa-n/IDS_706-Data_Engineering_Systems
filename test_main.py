"""test_main module"""
import main

def test_main():
    '''
    testing function for system
    '''
    assert not main.display_system_info().isEmpty()
