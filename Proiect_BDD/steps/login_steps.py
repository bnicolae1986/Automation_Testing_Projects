from behave import *

@given('I am on the login page')
def step_impl(context):
    context.login_page.navigate_to_page()

@when('I insert an username "{username}"')
def step_impl(context, username):
    context.login_page.set_email(username)

@when('I insert a password "{password}')
def step_impl(context, password):
    context.login_page.set_password(password)

@when('I dont insert an username')
def step_impl(context):
    context.login_page.no_email()

@when('I dont insert a password')
def step_impl(context):
    context.login_page.no_password()

@when('I click on the login button')
def step_impl(context):
    context.login_page.click_login()

@then('The message is "{message}"')
def step_impl(context, message):
    assert message in context.login_page.get_flash_container_message()

@when('I click on the logout button')
def step_impl(context):
    context.login_page.click_logout()

@then('The second message is "{message}"')
def step_impl(context, message):
    assert message in context.login_page.get_logout_flash_container_message()

@then('The third message is "{message}"')
def step_impl(context, message):
    assert message in context.login_page.get_logout_flash_container_message()

