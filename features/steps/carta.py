from behave import *


@given('a 50 $ orange juice')
def step_impl(context):
    pass

@given('a 400 $ full hamburguer')
def step_impl(context):
    pass

@given('the menu with items in it')
def step_impl(context):
    pass

@when('a customer accesss the site')
def step_impl(context):
    assert True is not False

@then('the menu with all items details is given')
def step_impl(context):
    assert context.failed is False

