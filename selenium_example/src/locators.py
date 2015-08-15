from selenium.webdriver.common.by import By


class MainViewPageLocators(object):
    GO_BUTTON = (By.ID, 'submit')
    NEW_FOLDER_BUTTON = (By.CSS_SELECTOR, 'button.folderoptions_toolbar_button.btn.btn-create-folder.enabled.'
                                          'first.last')
    CREATE_FOLDER_FIELD = (By.NAME, 'content_name')
    CREATE_FOLDER_BUTTON = (By.CSS_SELECTOR, '.ID-CREATE.btn.btn-small.btn-primary')
    MESSAGE = (By.XPATH, '//*[@id="error_msg_placeholder"]/div/p/span')


class LoginPageLocators(object):
    LOGIN_BUTTON = (By.ID, 'loginBtn')
    USERNAME_FIELD = (By.ID, 'j_username')
    PASSWORD_FIELD = (By.ID, 'j_password')
    REMEMBER_ME_CHECKBOX = (By.ID, 'remember')