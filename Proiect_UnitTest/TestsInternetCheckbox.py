import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestsCheckboxTheInternet(unittest.TestCase):


    URL = "https://the-internet.herokuapp.com/checkboxes"
    FIRST_CHECKBOX_SELECTOR = (By.CSS_SELECTOR, "form#checkboxes > input:nth-child(1)")
    SECOND_CHECKBOX_SELECTOR = (By.CSS_SELECTOR, "form#checkboxes > input:nth-of-type(2)")

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(self.URL)

    def tearDown(self):
        # close the driver
        self.driver.quit()

    def test_check_box(self):
        first_checkbox_element = self.driver.find_element(*self.FIRST_CHECKBOX_SELECTOR)
        assert first_checkbox_element.is_selected() == False, "First checkbox element not is selected at the beginning of the test"
        first_checkbox_element.click()
        assert first_checkbox_element.is_selected() == True, "First checkbox element is selected after clicking on the element"

        second_checkbox_element = self.driver.find_element(*self.SECOND_CHECKBOX_SELECTOR)
        assert second_checkbox_element.is_selected() == True, "Second checkobox is selected at the beginning at the test"
        second_checkbox_element.click()
        assert second_checkbox_element.is_selected() == False, "Second checkbox is not selected after clicking on the element"


