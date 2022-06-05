import pytest
from api import Moyklass
from settings import valid_email, valid_password
from settings import valid_date, valid_paid, valid_userId, valid_includeLessons
from settings import valid_includeBills, valid_includeUserSubscriptions, valid_limit, valid_offset, valid_sort


m = Moyklass()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = m.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_api_filials(date=valid_date, paid=valid_paid, userId=valid_userId, includeLessons=valid_includeLessons,
                         includeBills=valid_includeBills, includeUserSubscriptions=valid_includeUserSubscriptions,
                         limit=valid_limit, offset=valid_offset, sort=valid_sort):
    status, result = m.get_api_filials(date, paid, userId, includeLessons, includeBills, includeUserSubscriptions,
                                       limit, offset, sort)
    assert status == 200


