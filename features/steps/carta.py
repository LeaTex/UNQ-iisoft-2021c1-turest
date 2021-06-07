from behave import given, when, then
from administracion.models import Item
from django.contrib.auth.models import User


@given(u'there are no items registered in the system')
def items_list_is_empty(context):
    assert Item.objects.all().count() == 0


@given(u'the customer enter the home page')
def customer_enter_home_page(context):
    context.response = context.test.client.get('/')
    assert context.response.status_code == 200


@then(u'message "{message}" is displayed')
def empty_list_message_displayed(context, message):
    context.test.assertContains(context.response, message)


@given(u'there is a "{item_price}" dollar "{item_name}" with "{item_description}" in the menu')
def add_item_to_menu(context, item_price, item_name, item_description):
    User.objects.create_user(username='test_user', email='user@test.com', password='TestUser12345')
    Item.objects.create(author=User.objects.first(), name=item_name, description=item_description, price=float(item_price))
    assert Item.objects.all().count() != 0

@given(u'there are this three items')
def add_three_items_to_menu(context):
    User.objects.create_user(username='test_user', email='user@test.com', password='TestUser12345')
    for row in context.table:
        Item.objects.create(author=User.objects.first(), name=row['item_name'], description=row['item_description'], price=float(row['item_price']))
    assert Item.objects.all().count() == 3


@then(u'"{item_name}" is in menu')
def step_impl(context, item_name):
    context.test.assertContains(context.response, item_name)


@then(u'message "{message}" is not displayed')
def empty_list_message_displayed(context, message):
    context.test.assertNotContains(context.response, message)
