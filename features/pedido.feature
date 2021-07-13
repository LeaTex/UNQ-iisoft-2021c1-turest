Feature: Eliminar un item del pedido
  Como cliente quiero poder eliminar un item de un pedido para no tenerlo mas en la solicitud y que no me lo entreguen

  Scenario: customer deletes one item from the order with two items 
      Given an order with 1 milanesa and 2 helado
        When the customer clicks on eliminar button next to milanesa item 
       Then the order shows only 2 helado 
       But the order does not show 1 milanesa

  Scenario: customer deletes one item from the order with only one item  
      Given an order with 1 milanesa
        When the customer clicks on eliminar button next to milanesa item 
       Then the message "No hay productos agregados en tu pedido." is displayed

    