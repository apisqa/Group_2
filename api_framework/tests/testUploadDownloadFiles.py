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

    @classmethod
    def tearDownClass(cls):
        cls.calls.delete_test_files()

    def test_create_folder_positive(self):
        folder_name = self.calls.gen_random_name()
        resp = self.calls.create_folder(folder_name)
        assert resp.http_code == httplib.CREATED
        file1 = self.calls.gen_file()
        resp = self.calls.upload(file1)
        assert resp.http_code == httplib.OK

    def test_upload_file_as_power_user_not_enough_permission(self):
        perms = ['None', 'Viewer']
        for perm in perms:
            folder_name = self.calls.gen_random_name()
            file1 = self.calls.gen_file()
            resp = self.calls.create_folder(folder_name)
            assert resp.http_code == httplib.CREATED
            self.calls.set_perms(folder_name, perm, self.config.puser)
            resp = self.calls.upload(file1, path='%s/%s' % (self.config.test_path, folder_name), username=self.config.puser)
            assert resp.http_code == httplib.FORBIDDEN
            assert resp.body['message'] == 'You do not have permission to upload to this folder'

    def test_upload_file_as_power_user_enough_permission(self):
        perms = ['Editor', 'Full', 'Owner']
        for perm in perms:
            folder_name = self.calls.gen_random_name()
            file1 = self.calls.gen_file()
            resp = self.calls.create_folder(folder_name)
            assert resp.http_code == httplib.CREATED
            self.calls.set_perms(folder_name, perm, self.config.puser)
            resp = self.calls.upload(file1, path='%s/%s' % (self.config.test_path, folder_name), username=self.config.puser)
            assert resp.http_code == httplib.OK
            assert resp.body['checksum'] == resp.headers['x-sha512-checksum']
            assert resp.body['group_id']
            assert resp.body['entry_id']

    def test_no_user_set_perms(self):
        folder_name = self.calls.gen_random_name()
        resp = self.calls.create_folder(folder_name)
        assert resp.http_code == httplib.CREATED
        resp = self.calls.set_perms(folder_name, 'Full', 'asdasdasd')
        assert resp.http_code == httplib.OK

    def test_upload_file_with_duplicate_name_of_folder(self):
        folder_name = self.calls.gen_random_name()
        self.calls.create_folder(folder_name)
        file1 = self.calls.gen_file(folder_name)
        resp = self.calls.upload(file1)
        assert resp.http_code == httplib.FORBIDDEN
        assert resp.body['message'] == 'A folder with the same name already exists: %s%s' % (self.config.test_path,
                                                                                             folder_name)

    def test_download_file_positive(self):
        folder_name = self.calls.gen_random_name()
        self.calls.create_folder(folder_name)
        file1 = self.calls.gen_file()
        self.calls.upload(file1)
        resp = self.calls.download(file1)
        file2 = resp.body
        assert self.calls.compare(file1, file2)

    def test_download_non_existent_file(self):
        file1 = self.calls.gen_file()
        resp = self.calls.download(file1)
        assert resp.http_code == httplib.NOT_FOUND
        assert resp.body['message'] == 'File does not exist'