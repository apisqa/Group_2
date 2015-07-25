import requests
import json


def create_folder(path, domain=None, username=None, password=None,
                  content_type=None, accept=None, method=None):
    if domain is None:
        domain = 'https://istepanko.qa-egnyte.com'
    if content_type is None:
        content_type = 'application/json'
    if username is None:
        username = 'istepanko'
    if password is None:
        password = 'apitest2'
    if method is None:
        method = 'POST'
    if accept is None:
        accept = 'application/json'

    endpoint = '/public-api/v1/fs'
    url = domain + endpoint + path
    headers = dict()
    headers['Content-Type'] = content_type
    headers['Accept'] = accept
    data = dict()
    data['action'] = 'add_folder'
    data = json.dumps(data)
    r = requests.request(
        url=url,
        auth=(username, password),
        headers=headers,
        data=data,
        method=method
    )
    return r

resp = create_folder()
data = resp.content
status_code = resp.status_code
headers = resp.headers
print('\n'
      'Data:'
      '\n'
      '%s'
      '\n'
      'Status_code:'
      '\n'
      '%s'
      '\n'
      'Headers:'
      '\n'
      '%s' % (resp.content, resp.status_code, resp.headers))