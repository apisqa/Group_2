from api_utils import Calls
from unittest import TestCase
import httplib


class TestClass(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calls = Calls()

    def test_create_folder_positive(self):
        resp = self.calls.create_folder('test_folder1')
        assert resp.status_code == httplib.CREATED