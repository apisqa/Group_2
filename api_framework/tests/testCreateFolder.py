from api_utils import Calls
from unittest import TestCase
import httplib


# Defining TestClass class using inheritance from TestCase class of module unittest
class TestClass(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calls = Calls()
        print('setUpClass executed')

    def test_create_folder_positive(self):
        folder_name = self.calls.gen_random_name()
        resp = self.calls.create_folder(folder_name)
        assert resp.http_code == httplib.CREATED
        self.calls.delete_folder(folder_name)

    def test_delete_folder(self):
        folder = self.calls.gen_random_name()
        resp = self.calls.create_folder(folder)
        assert resp.http_code == httplib.CREATED
        resp = self.calls.delete_folder(folder)
        assert resp.http_code == httplib.OK

    def test_create_folder_incorrect_credentials(self):
        folder = self.calls.gen_random_name()
        resp = self.calls.create_folder(folder, password='asdas')
        assert resp.http_code == httplib.UNAUTHORIZED
        assert resp.body['inputErrors']['credentials'][0]['code'] == 'INVALID_CREDENTIALS'
        assert resp.body['inputErrors']['credentials'][0]['msg'] == 'This request is unauthenticated. Please provide ' \
                                                                    'credentials and try again.'

    def test_delete_non_existent_folder(self):
        folder_name = self.calls.gen_random_name()
        resp = self.calls.delete_folder(folder_name)
        assert resp.http_code == httplib.NOT_FOUND