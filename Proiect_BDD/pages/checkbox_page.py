from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckBox(BasePage):

    URL = "https://the-internet.herokuapp.com/checkboxes"
    FIRST_CHECKBOX_SELECTOR = (By.CSS_SELECTOR, "form#checkboxes > input:nth-child(1)")
    SECOND_CHECKBOX_SELECTOR = (By.CSS_SELECTOR, "form#checkboxes > input:nth-of-type(2)")


    def navigate_to_page(self):
        self.driver.get(self.URL)

    def click_on_first_checkbox(self):
        self.click(self.FIRST_CHECKBOX_SELECTOR)

    def click_on_second_checkbox(self):
        self.click(self.SECOND_CHECKBOX_SELECTOR)

    def first_checkbox_selected(self):
        first_checkbox = self.driver.find_element(*self.FIRST_CHECKBOX_SELECTOR)
        return first_checkbox.is_selected()

    def second_checkbox_unselected(self):
        second_checkbox = self.driver.find_element(*self.SECOND_CHECKBOX_SELECTOR)
        return not second_checkbox.is_selected()
