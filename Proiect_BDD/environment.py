from driver import Driver
from pages.login_page import LoginPage
from pages.alerts_page import AlertsPage
from pages.checkbox_page import CheckBox

def before_all(context):
    context.browser = Driver()
    context.login_page = LoginPage()
    context.alerts_page = AlertsPage()
    context.checkbox_page = CheckBox()

def after_all(context):
    context.browser.close()

