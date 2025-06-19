# Created by rekhagujalwar at 6/9/25
Feature: Cart Tests
  # Enter feature description here

  Scenario: Target shopping cart verification
    Given Open target main page
    When Clicked on Shopping cart icon
    Then Verify that the shopping cart is empty


    # Created by rekhagujalwar at 6/12/25 ---> HW_4

  Scenario: Verify that the added product is available in the cart
    Given Open target main page
    When Search for tea
    And Click on Add to Cart button
    And Click on Shopping cart icon
    Then Verify that the added product is available in the Cart

