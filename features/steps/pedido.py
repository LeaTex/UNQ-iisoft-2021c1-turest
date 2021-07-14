from behave import given, when, then
from administracion.models import Item
from django.contrib.auth.models import User

@given(u'a menu with a "{mila_price}" pesos "{mila_item_name}" and "{helado_price}" pesos "{helado_item_name}"')
def menu_with_two_items(context, mila_item_name, mila_price, helado_item_name, helado_price):
    User.objects.create_user(username='test_user', email='user@test.com', password='TestUser12345')
    Item.objects.create(author=User.objects.first(), name=mila_item_name, description=mila_item_name, price=int(mila_price))
    Item.objects.create(author=User.objects.first(), name=helado_item_name, description=helado_item_name, price=int(helado_price))
    assert Item.objects.all().count() == 2


@given(u'an order with "{mila_amount}" "{mila_item_name}" and "{helado_amount}" "{helado_item_name}" of "{total_cost}" pesos total cost')
def order_with_two_items(context, mila_amount, mila_item_name, helado_amount, helado_item_name, total_cost):

    item = Item.objects.filter(name=mila_item_name).first()
    context.test.client.post(f'/itemView/{item.id}/', {'cantidad': int(mila_amount), 'item': item.id})

    item = Item.objects.filter(name=helado_item_name).first()
    context.test.client.post(f'/itemView/{item.id}/', {'cantidad': int(helado_amount), 'item': item.id})

    context.response = context.test.client.get('/cartView/')
    print(str(context.response.content))
    context.test.assertContains(context.response, f'({mila_amount}) {mila_item_name}')
    context.test.assertContains(context.response, f'({helado_amount}) {helado_item_name}')
    context.test.assertContains(context.response, f'{total_cost}')


@when(u'the customer clicks on "{delete_item_btn}" button next to "{mila_item_name}" item')
def step_impl(context, delete_item_btn, mila_item_name):
    # opción 1:
    # buscar el link/botón y hacerle clic
    # complicada sin selenium

    # opción 2:
    # emular el click utilizando el request
    # el primer elemento del pedido tiene id 0
    context.response = context.test.client.get('/cartItemDelete/0/')
    assert context.response.status_code == 302 # redirect


@then(u'the order shows only "{helado_amount}" "{helado_item_name}" of "{total_cost}" pesos total cost')
def updated_order_with_one_item(context, helado_amount, helado_item_name, total_cost):
    context.response = context.test.client.get('/cartView/')

    context.test.assertContains(context.response, f'({helado_amount}) {helado_item_name}')
    context.test.assertContains(context.response, f'{total_cost}')


@then(u'the order does not show any "{mila_item_name}"')
def updated_order_without_deleted_item(context, mila_item_name):
    context.test.assertNotContains(context.response, mila_item_name)
