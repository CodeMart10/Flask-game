import pytest
from game import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_username(client):
    response = client.get('/')
    client.post('/', data={'username': 'test'})

def test_rooms(client):
    response = client.get('engine/Tank')
    assert 'http://localhost/engine/Tank' == response.headers['Location']
