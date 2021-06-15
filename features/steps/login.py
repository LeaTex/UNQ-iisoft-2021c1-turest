from behave import given, when, then
from django.contrib.auth.models import User
from selenium import webdriver
import time


@given(u'the user "{customer_nickname}" is registered in system with password "{customer_pass}"')
def register_user(context, customer_nickname, customer_pass):
    context.user = User.objects.create_user(username=customer_nickname, email='user@test.com', password=customer_pass)
    assert User.objects.all().count() != 0


@given(u'the customer go to login page at "{login_url}"')
def goto_login_page(context, login_url):
    context.driver = webdriver.Chrome()
    time.sleep(2)
    context.driver.get(context.get_url(login_url))
    time.sleep(1)


@when(u'the customer completes username "{customer_nickname}" and password "{customer_pass}" and clicks "Entrar"')
def fill_login_form(context, customer_nickname, customer_pass):
    context.driver.find_element_by_name("username").send_keys(customer_nickname)
    context.driver.find_element_by_name("password").send_keys(customer_pass)
    time.sleep(1)
    context.driver.find_element_by_xpath('//button[text()="Ingresar"]').click()


@then(u'menu with message "{welcome}" "{customer_nickname}" is displayed')
def welcome_message_displayed(context, welcome, customer_nickname):
    welcome_message = '{} {}'.format(welcome, customer_nickname)
    assert welcome_message in context.driver.page_source


@then(u'error message "{not_welcome}" is displayed')
def login_error_message_displayed(context, not_welcome):
    assert not_welcome in context.driver.page_source
