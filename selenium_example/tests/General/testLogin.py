import unittest
from selenium import webdriver
import page


class TestClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://istepanko.qa-egnyte.com')

    def test_search_in_python_org(self):
        login_page = page.LoginPage(self.driver)
        assert login_page.is_title_matches()
        #login_page.search_text_element = "pycon"
        login_page.put_text_to_username_field('istepanko')
        login_page.put_text_to_password_field('egnyte4you')
        login_page.click_login_button()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()