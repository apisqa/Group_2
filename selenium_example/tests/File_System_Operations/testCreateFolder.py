import unittest
from selenium import webdriver
import page
from utils import SmartSearch


class TestClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://istepanko.qa-egnyte.com')

    def test_create_folder_positive(self):
        test_page = page.LoginPage(self.driver)
        assert test_page.is_title_matches()
        test_page.login()
        test_page = page.MainViewPage(self.driver)
        test_page.create_folder('test')
        assert test_page.get_message_text() == '"test" folder created. Share this folder.'

    def test_create_folder_special_characters(self):
        test_page = page.LoginPage(self.driver)
        assert test_page.is_title_matches()
        test_page.login()
        test_page = page.MainViewPage(self.driver)
        test_page.create_folder(' !@#$%^&test')
        assert test_page.get_message_text() == '"test" folder created. Share this folder.'

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()