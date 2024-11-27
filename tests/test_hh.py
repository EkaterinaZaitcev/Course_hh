from src.hh import HH
from unittest.mock import patch


@patch("requests.get")
def test_hh(test_requests_api):

    obj_api = HH()
    assert type(obj_api) is HH