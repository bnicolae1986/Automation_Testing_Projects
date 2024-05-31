from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:

    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    driver.maximize_window()

    def close(self):
        self.driver.quit()



