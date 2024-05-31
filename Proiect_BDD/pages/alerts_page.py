from selenium.webdriver.common import alert

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AlertsPage(BasePage):

    URL = "https://the-internet.herokuapp.com/javascript_alerts"
    ALERT_SELECTOR = (By.XPATH, "//button[contains(text(), 'Click for JS Alert')]")
    ALERT_CONFIRM_SELECTOR = (By.XPATH, "//button[contains(text(), 'Click for JS Confirm')]")
    ALERT_PROMPT_SELECTOR = (By.XPATH, "//button[contains(text(), 'Click for JS Prompt')]")
    RESULT_SELECTOR = (By.ID, "result")

    def navigate_to_page(self):
        self.driver.get(self.URL)

    def click_on_alert(self):
        self.click(self.ALERT_SELECTOR)

    def click_dismiss_alert(self):
        self.click(self.ALERT_CONFIRM_SELECTOR)

    def switch_and_accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def switch_and_dismiss_alert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def prompt_alert(self):
        self.click(self.ALERT_PROMPT_SELECTOR)

    def prompt_enter_text(self, text):
        alert = self.driver.switch_to.alert
        alert.send_keys(text)

    def get_result_text(self):
        return self.get_element_text(self.RESULT_SELECTOR)






























