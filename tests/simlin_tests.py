from nose.tools import *
from simlin.simlin import * 

'''
def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"
'''

def test_list():
    '''test that a list is returned'''
    l = list_images()
    assert type(l) == list
