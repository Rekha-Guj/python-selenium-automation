# Created by rekhagujalwar at 6/5/25
Feature: target shopping cart
  # verifying if the shopping cart is empty

  Scenario: Target shopping cart verification
    Given Target main page is open
    When Clicked on Shopping cart icon
    Then Verify that the shopping cart is empty