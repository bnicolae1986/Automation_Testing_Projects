from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    #constante
    URL = "https://the-internet.herokuapp.com/login"
    USERNAME_ELEMENT_LOCATOR = (By.CSS_SELECTOR, "#username")
    PASSWORD_ELEMENT_LOCATOR = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON_LOCATOR = (By.CLASS_NAME, "radius")
    LOGOUT_BUTTON_LOCATOR = (By.CLASS_NAME, "icon-signout")
    LOGIN_FLASH_CONTAINER_LOCATOR = (By.ID, "flash-messages")
    LOGOUT_FLASH_CONTAINER_LOCATOR = (By.ID, "flash")
    INVALID_PASSWORD_CONTAINER_LOCATOR = (By.CLASS_NAME, "flash error")

    def navigate_to_page(self):
        self.driver.get(self.URL)

    def set_email(self, given_email):
        self.type(self.USERNAME_ELEMENT_LOCATOR, given_email)

    def no_email(self):
        self.click(self.USERNAME_ELEMENT_LOCATOR)

    def no_password(self):
        self.click(self.PASSWORD_ELEMENT_LOCATOR)

    def set_password(self, given_password):
        self.type(self.PASSWORD_ELEMENT_LOCATOR, given_password)

    def click_login(self):
        #self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR).click()
        self.click(self.LOGIN_BUTTON_LOCATOR)

    def click_logout(self):
        self.click(self.LOGOUT_BUTTON_LOCATOR)

    def get_flash_container_message(self):
        return self.get_element_text(self.LOGIN_FLASH_CONTAINER_LOCATOR)

    def get_logout_flash_container_message(self):
        return self.get_element_text(self.LOGOUT_FLASH_CONTAINER_LOCATOR)

    def get_invalid_password_flash_container_message(self):
        return self.get_element_text(self.INVALID_PASSWORD_CONTAINER_LOCATOR)