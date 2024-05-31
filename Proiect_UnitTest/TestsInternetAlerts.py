import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

#comentariu
class TestsAlertsTheInternet(unittest.TestCase):

    URL = "https://the-internet.herokuapp.com/javascript_alerts"
    ALERT_SELECTOR = (By.XPATH, "//button[contains(text(), 'Click for JS Alert')]")
    ALERT_CONFIRM_SELECTOR = (By.XPATH, "//button[contains(text(), 'Click for JS Confirm')]")
    ALERT_PROMPT_SELECTOR = (By.XPATH, "//button[contains(text(), 'Click for JS Prompt')]")
    RESULT_SELECTOR = (By.ID, "result")

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()


    def test_alert_ok(self):
        alert_button = self.driver.find_element(*self.ALERT_SELECTOR)
        alert_button.click()
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert_element = self.driver.switch_to.alert
        alert_element.accept()
        result_element = self.driver.find_element(*self.RESULT_SELECTOR)
        result_element_text = result_element.text
        assert "You successfully clicked an alert" in result_element_text

    def test_alert_confirm(self):
        alert_button = self.driver.find_element(*self.ALERT_CONFIRM_SELECTOR)
        alert_button.click()
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert_element = self.driver.switch_to.alert
        alert_element.accept()
        result_element = self.driver.find_element(*self.RESULT_SELECTOR)
        result_element_text = result_element.text
        assert "You clicked: Ok" in result_element_text

    def test_alert_decline(self):
        alert_button = self.driver.find_element(*self.ALERT_CONFIRM_SELECTOR)
        alert_button.click()
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert_element = self.driver.switch_to.alert
        alert_element.dismiss()
        result_element = self.driver.find_element(*self.RESULT_SELECTOR)
        result_element_text = result_element.text
        assert "You clicked: Cancel" in result_element_text

    def test_text_prompt_ok(self):
        alert_button = self.driver.find_element(*self.ALERT_PROMPT_SELECTOR)
        alert_button.click()
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert_element = self.driver.switch_to.alert
        alert_element.send_keys("bogdan")
        alert_element.accept()
        result_element = self.driver.find_element(*self.RESULT_SELECTOR)
        result_element_text = result_element.text
        assert "You entered: bogdan" in result_element_text

    def test_text_prompt_dismiss(self):
        alert_button = self.driver.find_element(*self.ALERT_PROMPT_SELECTOR)
        alert_button.click()
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert_element = self.driver.switch_to.alert
        alert_element.send_keys("bogdan")
        alert_element.dismiss()
        result_element = self.driver.find_element(*self.RESULT_SELECTOR)
        result_element_text = result_element.text
        assert "You entered: null" in result_element_text

    def test_no_text_ok(self):
        alert_button = self.driver.find_element(*self.ALERT_PROMPT_SELECTOR)
        alert_button.click()
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert_element = self.driver.switch_to.alert
        alert_element.accept()
        result_element = self.driver.find_element(*self.RESULT_SELECTOR)
        result_element_text = result_element.text
        assert "" in result_element_text

    def test_no_text_dismiss(self):
        alert_button = self.driver.find_element(*self.ALERT_PROMPT_SELECTOR)
        alert_button.click()
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert_element = self.driver.switch_to.alert
        alert_element.dismiss()
        result_element = self.driver.find_element(*self.RESULT_SELECTOR)
        result_element_text = result_element.text
        assert "You entered: null" in result_element_text

