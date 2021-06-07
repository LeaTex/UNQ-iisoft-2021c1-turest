Feature: Acceder a la carta menú
  Como usuario quiero acceder al menú para conocer la oferta del día.

  Scenario: customer enter the site and no items are in menu
      Given there are no items registered in the system
        And the customer enter the home page
       Then message "No hay ítems cargados." is displayed

  Scenario: customer enter the site and there is one item in menu
      Given there is a "15" dollar "pizza" with "tomatoes and olives" in the menu
        And the customer enter the home page
       Then "pizza" is in menu
        But message "No hay ítems cargados." is not displayed

  Scenario: customer enter the site and there are three items in menu
      Given there are this three items
        | item_name | item_description  | item_price |
        | milk      | sweet coat milk   | 10         |
        | bread     | toasted and tasty | 15         |
        | honey     | sweet and sticky  | 12.5       |

        And the customer enter the home page
       Then "milk" is in menu
        And "bread" is in menu
        And "honey" is in menu
