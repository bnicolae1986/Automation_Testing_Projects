from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver import Driver

class BasePage(Driver):

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def type(self, locator, text):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)


    def wait_for_element(self, locator, wait_time) -> WebElement:
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.presence_of_element_located(locator))

    def get_element_text(self, locator):
        return self.wait_for_element(locator, 10).text



    # behave pt a rula testele in terminal
    # behave --tags=positive
    # behave-html-formatter de instalat
    # behave.ini cu cele 2 linii de cod
    # pt raport behave -f html -o raport.html
    # pt raport behave -f html -o raport.html --tags=login










