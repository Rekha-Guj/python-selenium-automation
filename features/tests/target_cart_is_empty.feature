# Created by rekhagujalwar at 6/5/25 ---> HW_3
Feature: target shopping cart
  # verifying if the shopping cart is empty

  Scenario: Target shopping cart verification
    Given Open target main page
    When Clicked on Shopping cart icon
    Then Verify that the shopping cart is empty
    Then Verify Cart page is open