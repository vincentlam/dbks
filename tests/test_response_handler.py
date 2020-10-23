import pytest
from requests import Response
from unittest.mock import MagicMock
from dbks.response_handler import ResponseHandler

success = MagicMock(spec=Response)
success.status_code = 200

failed = MagicMock(spec=Response)
failed.status_code = 400


class A:
    @ResponseHandler
    def method_1(self):
        return success

    @ResponseHandler
    def method_2(self):
        return failed


a = A()


def test_response_handler_success():
    assert a.method_1().status_code == 200


def test_response_handler_failed():
    with pytest.raises(SystemError):
        a.method_2()
