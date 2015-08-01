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
        assert resp.http_code == httplib.CREATED

    def test_create_folder_incorrect_credentials(self):
        folder = self.calls.gen_random_name()
        resp = self.calls.create_folder(folder, password='asdas')
        assert resp.http_code == httplib.UNAUTHORIZED
        assert resp.json['inputErrors']['credentials'][0]['code'] == 'INVALID_CREDENTIALS'
        assert resp.json['inputErrors']['credentials'][0]['msg'] == 'This request is unauthenticated. Please provide ' \
                                                                    'credentials and try again.'
