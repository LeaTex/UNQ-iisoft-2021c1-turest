Feature: Eliminar un item del pedido
  Como cliente quiero poder eliminar un item de un pedido para no tenerlo mas en la solicitud y que no me lo entreguen

  Background: the menu has items
      Given a menu with a "150" pesos "milanesa" and "85" pesos "helado"

  Scenario: customer deletes one item from the order with two items 
      Given an order with "1" "milanesa" and "2" "helado" of "320" pesos total cost
       When the customer clicks on "Eliminar" button next to "milanesa" item
       Then the order shows only "2" "helado" of "170" pesos total cost
        But the order does not show any "milanesa"

  Scenario: customer deletes one item from the order with only one item  
      Given an order with "1" "milanesa" of "150" pesos total cost
       When the customer clicks on "Eliminar" button next to "milanesa" item
       Then the message "No hay productos agregados en tu pedido." is displayed
