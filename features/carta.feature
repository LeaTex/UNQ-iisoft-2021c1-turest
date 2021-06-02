Feature: restaurant menu
  the menu is the main component of the system, and the essence of any gastronomic business.

  Background: there are items in the system
    Given a 50 $ orange juice
      And a 400 $ full hamburguer

  Scenario: the menu shows all available items to order
      Given the menu with items in it
       When a customer accesss the site
       Then the menu with all items details is given
