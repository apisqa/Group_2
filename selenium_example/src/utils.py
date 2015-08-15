from selenium import webdriver
from time import sleep
from ConfigParser import SafeConfigParser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class Config:
    def __init__(self):
        parser = SafeConfigParser()
        parser.read('config.ini')
        self.domain = parser.get('Config', 'domain')
        self.admin_login = parser.get('Config', 'admin_login')
        self.admin_password = parser.get('Config', 'admin_password')

    def print_config(self):
        for prop in self.__dict__:
            print('%s = %s' % (prop, self.__dict__.get(prop)))


class SmartSearch:
    def __init__(self, driver):
        self.driver = driver
        self.wait = 20

    def smart_find(self, by, value):
        try:
            WebDriverWait(self.driver, self.wait).until(ec.presence_of_all_elements_located((by, value)))
        finally:
            elem = self.driver.find_element(by, value)
        return elem