import requests
import json
from ConfigParser import SafeConfigParser
import os


class Config:
    def __init__(self):
        self.parser = SafeConfigParser()
        if os.path.isfile('config.ini'):
            self.parser.read('config.ini')
        else:
            print('No config.ini found under root folder.')
        self.domain = self.parser.get('Server', 'domain')
        self.admin_login = self.parser.get('Server', 'admin')
        self.password = self.parser.get('Server', 'password')

f = Config()
print(f.admin_login)