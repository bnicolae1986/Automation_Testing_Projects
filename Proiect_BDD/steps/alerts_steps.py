from behave import *

@given('I am on the alerts page')
def step_impl(context):
    context.alerts_page.navigate_to_page()

@when('I click on OK alert button')
def step_impl(context):
    context.alerts_page.click_on_alert()

@when('I click on Confirm alert button')
def step_impl(context):
    context.alerts_page.click_dismiss_alert()

@when('I click on Prompt alert button')
def step_impl(context):
    context.alerts_page.prompt_alert()

@when('I enter text "bogdan"')
def step_impl(context):
    context.alerts_page.prompt_enter_text("bogdan")

@when('I do not enter text')
def step_impl(context):
    context.alerts_page.prompt_enter_text("")

@when('I accept alert')
def step_impl(context):
    context.alerts_page.switch_and_accept_alert()

@when('I dismiss alert')
def step_impl(context):
    context.alerts_page.switch_and_dismiss_alert()

@then('The message3 displayed is "{message3}"')
def step_impl(context, message3):
    assert message3 in context.alerts_page.get_result_text()

@then('The message4 displayed is "{message4}"')
def step_impl(context, message4):
    assert message4 in context.alerts_page.get_result_text()

@then('The message5 displayed is "{message5}"')
def step_impl(context, message5):
    assert message5 in context.alerts_page.get_result_text()

@then('The message displayed is "{message2}"')
def step_impl(context, message2):
    assert message2 in context.alerts_page.get_result_text()

@then('The message for alerts page is "{message}"')
def step_impl(context, message):
    assert message in context.alerts_page.get_result_text()















