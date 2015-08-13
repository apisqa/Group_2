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
        self.assertEqual(resp.http_code, httplib.CREATED)
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
        assert resp.body['errorMessage'] == 'Item does not exist'

# Demanding wrong content_type from the server
    def test_delete_folder_wrong_accept_header(self):
        folder_name = self.calls.gen_random_name()
        resp = self.calls.delete_folder(folder_name, accept='application/xml')
        assert resp.http_code == httplib.NOT_ACCEPTABLE
        assert resp.body['errorMessage'] == 'Not Acceptable'

    def test_method_not_allowed(self):
        resp = self.calls.delete_folder(self.calls.gen_random_name(), method='UPDATE')
        assert resp.http_code == httplib.METHOD_NOT_ALLOWED
        assert resp.body['errorMessage'] == 'Method Not Allowed'

    def test_wrong_content_type(self):
        resp = self.calls.create_folder(self.calls.gen_random_name(), content_type='application/xml')
        assert resp.http_code == httplib.UNSUPPORTED_MEDIA_TYPE
        assert resp.body['errorMessage'] == 'Unsupported Media Type'

    def test_create_and_delete_100_folders_in_a_row(self):
        folder_name = self.calls.gen_random_name()
        for i in range(10):
            resp = self.calls.create_folder(folder_name + str(i))
            assert resp.http_code == httplib.CREATED
            assert resp.body == self.calls.no_json
        for i in range(10):
            resp = self.calls.delete_folder(folder_name + str(i))
            assert resp.http_code == httplib.OK
            assert resp.body == self.calls.no_json

    def test_perms(self):
        folder_name = self.calls.gen_random_name()
        self.calls.create_folder(folder_name)
        resp = self.calls.set_perms(folder_name, user=self.config.puser, permission='Full')
        assert resp.http_code == httplib.OK
        resp = self.calls.create_folder(folder_name, username=self.config.puser, test_path='%s/%s' %
                                                                                           (self.config.test_path, folder_name))
        assert resp.http_code == httplib.CREATED