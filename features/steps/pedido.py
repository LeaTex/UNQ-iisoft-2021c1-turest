from behave import given, when, then
from administracion.models import Item
from django.contrib.auth.models import User

@given(u'an order with 1 milanesa and 2 helado')
def step_impl(context):
    context.response = context.test.client.get('cartView/')
    assert context.response.status_code == 200


@when(u'the customer clicks on eliminar button next to milanesa item')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the customer clicks on eliminar button next to milanesa item')


@then(u'the order shows only 2 helado')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the order shows only 2 helado')


@then(u'the order does not show 1 milanesa')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the order does not show 1 milanesa')


@given(u'an order with 1 milanesa')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given an order with 1 milanesa')


@then(u'the message "{message}" is displayed')
def step_impl(context,message):
    context.test.assertContains(context.response, message)
