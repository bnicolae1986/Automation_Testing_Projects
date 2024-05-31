import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class TestsLoginTheInternet(unittest.TestCase):

    URL = "https://the-internet.herokuapp.com/login"
    USERNAME_ELEMENT_SELECTOR = (By.CSS_SELECTOR, "#username")
    PASSWORD_ELEMENT_SELECTOR = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON_ELEMENT_SELECTOR = (By.CLASS_NAME, "fa-sign-in")
    FLASH_CONTAINER_SELECTOR = (By.ID, "flash")
    LOGOUT_BUTTON_ELEMENT_SELECTOR = (By.CLASS_NAME, "icon-signout")
    LOGOUT_CONTAINER_SELECTOR = (By.ID, "flash")

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

# comanda terminal python -m unittest TestsInternetLogin.py
# comanda terminal python -m unittest *.py pentru a rula toate fisierele .py

    def test_negative_login(self):
        username_element = self.driver.find_element(*self.USERNAME_ELEMENT_SELECTOR)
        password_element = self.driver.find_element(*self.PASSWORD_ELEMENT_SELECTOR)
        login_button_element = self.driver.find_element(*self.LOGIN_BUTTON_ELEMENT_SELECTOR)
        username_element.click()
        username_element.clear()
        username_element.send_keys("bogdan@gmail.com")
        time.sleep(1)
        password_element.click()
        password_element.clear()
        password_element.send_keys("parola")
        time.sleep(1)
        login_button_element.click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FLASH_CONTAINER_SELECTOR))
        flash_container = self.driver.find_element(*self.FLASH_CONTAINER_SELECTOR)
        flash_container_text = flash_container.text
        assert "Your username is invalid!" in flash_container_text


    #@unittest.skip
    def test_positive_login(self):
        username_element = self.driver.find_element(*self.USERNAME_ELEMENT_SELECTOR)
        password_element = self.driver.find_element(*self.PASSWORD_ELEMENT_SELECTOR)
        login_button_element = self.driver.find_element(*self.LOGIN_BUTTON_ELEMENT_SELECTOR)
        username_element.click()
        username_element.clear()
        username_element.send_keys("tomsmith")
        time.sleep(1)
        password_element.click()
        password_element.clear()
        password_element.send_keys("SuperSecretPassword!")
        time.sleep(1)
        login_button_element.click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FLASH_CONTAINER_SELECTOR))
        flash_container = self.driver.find_element(*self.FLASH_CONTAINER_SELECTOR)
        flash_container_text = flash_container.text
        assert "You logged into a secure area!" in flash_container_text


    def test_logout(self):
        username_element = self.driver.find_element(*self.USERNAME_ELEMENT_SELECTOR)
        password_element = self.driver.find_element(*self.PASSWORD_ELEMENT_SELECTOR)
        login_button_element = self.driver.find_element(*self.LOGIN_BUTTON_ELEMENT_SELECTOR)
        username_element.click()
        username_element.clear()
        username_element.send_keys("tomsmith")
        time.sleep(1)
        password_element.click()
        password_element.clear()
        password_element.send_keys("SuperSecretPassword!")
        time.sleep(1)
        login_button_element.click()
        time.sleep(1)
        logout_button_element = self.driver.find_element(*self.LOGOUT_BUTTON_ELEMENT_SELECTOR)
        logout_button_element.click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOGOUT_CONTAINER_SELECTOR))
        flash_container = self.driver.find_element(*self.LOGOUT_CONTAINER_SELECTOR)
        flash_container_text = flash_container.text
        assert "You logged out of the secure area!" in flash_container_text

#tema cu carturesti de facut cu unittest?? 02-27 ne explica putin

    def test_negative_login_wrong_username(self):
        username_element = self.driver.find_element(*self.USERNAME_ELEMENT_SELECTOR)
        password_element = self.driver.find_element(*self.PASSWORD_ELEMENT_SELECTOR)
        login_element = self.driver.find_element(*self.LOGIN_BUTTON_ELEMENT_SELECTOR)
        username_element.click()
        username_element.clear()
        username_element.send_keys("bogdan@yahoo.com")
        time.sleep(1)
        password_element.click()
        password_element.clear()
        password_element.send_keys("SuperSecretPassword!")
        time.sleep(1)
        login_element.click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FLASH_CONTAINER_SELECTOR))
        flash_container = self.driver.find_element(*self.FLASH_CONTAINER_SELECTOR)
        flash_container_text = flash_container.text
        assert "Your username is invalid!" in flash_container_text


    def test_negative_login_wrong_password(self):
        username_element = self.driver.find_element(*self.USERNAME_ELEMENT_SELECTOR)
        password_element = self.driver.find_element(*self.PASSWORD_ELEMENT_SELECTOR)
        login_element = self.driver.find_element(*self.LOGIN_BUTTON_ELEMENT_SELECTOR)
        username_element.click()
        username_element.clear()
        username_element.send_keys("tomsmith")
        time.sleep(1)
        password_element.click()
        password_element.clear()
        password_element.send_keys("parola")
        time.sleep(1)
        login_element.click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FLASH_CONTAINER_SELECTOR))
        flash_container = self.driver.find_element(*self.FLASH_CONTAINER_SELECTOR)
        flash_container_text = flash_container.text
        assert "Your password is invalid!" in flash_container_text


