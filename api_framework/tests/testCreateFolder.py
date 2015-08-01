from api_utils import Calls
from unittest import TestCase
import httplib


class TestClass(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calls = Calls()

    def test_create_folder_positive(self):
        folder = self.calls.gen_random_name()
        resp = self.calls.create_folder(folder)
        assert resp.status_code == httplib.CREATED

    def test_create_folder_incorrect_credentials(self):
        folder = self.calls.gen_random_name()
        resp = self.calls.create_folder(folder, password='asdas')
        assert resp.status_code == httplib.UNAUTHORIZED
        assert resp.content['inputErrors']['credentials'] == 1