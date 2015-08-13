from api_utils import Calls
from api_utils import Config
from unittest import TestCase
import httplib


# Defining TestClass class using inheritance from TestCase class of module unittest
class TestClass(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calls = Calls()
        cls.config = Config()

    def test_create_folder_positive(self):
        folder_name = self.calls.gen_random_name()
        resp = self.calls.create_folder(folder_name)
        assert resp.http_code == httplib.CREATED
        file1 = self.calls.gen_file()
        resp = self.calls.upload(file1)
        assert resp.http_code == httplib.OK