# Created by rekhagujalwar at 6/4/25
Feature: Tests for target search
  # search a product

  Scenario: User can search for a product on target
    Given Open target main page
    When Search for tea
    Then Verify search worked


  Scenario: User can search for a product on target
    Given Open target main page
#    When Search for coffee
#    Then Verify search for coffee worked

