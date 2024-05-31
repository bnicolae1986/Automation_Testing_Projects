from behave import *

@given('I am on the checkbox page')
def step_impl(context):
    context.checkbox_page.navigate_to_page()

@when('I click on the first checkbox')
def step_impl(context):
    context.checkbox_page.click_on_first_checkbox()

@when('I click on the second checkbox')
def step_impl(context):
    context.checkbox_page.click_on_second_checkbox()

@then('The checkbox is selected')
def step_impl(context):
    assert context.checkbox_page.first_checkbox_selected()

@then('The checkbox is unselected')
def step_impl(context):
    assert context.checkbox_page.second_checkbox_unselected()

