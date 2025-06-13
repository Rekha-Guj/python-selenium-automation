# Created by rekhagujalwar at 6/12/25 ---> HW_4
Feature: Product verification in the cart

  Scenario: Verify that the added product is available in the cart
    Given Open target main page
    When Search for tea
    Then Click on Add to Cart button
    Then Click on Shopping cart icon
    Then Verify that the added product is available in the Cart