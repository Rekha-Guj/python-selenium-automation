# Created by rekhagujalwar at 6/9/25
Feature: Cart Tests
  # Enter feature description here

  Scenario: Target shopping cart verification
    Given Open target main page
    When Clicked on Shopping cart icon
    Then Verify that the shopping cart is empty