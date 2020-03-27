import pytest
from game import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_index(client):
    response = client.get('/')
    client.post('/', data={'username': 'test'})


## write more testsssss
