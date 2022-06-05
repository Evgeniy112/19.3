import pytest
from api import Moyklass
from settings import valid_email, valid_password

m = Moyklass()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = m.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

