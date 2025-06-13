# Created by rekhagujalwar at 6/4/25 ---> HW_1
Feature: Tests for target search
  # search a product

#  Scenario: User can search for a product on target
#    Given Open target main page
#    When Search for tea
#    Then Verify search worked for tea

# Scenario: User can search for a mug on target
#    Given Open target main page
#    When Search for mug
#    Then Verify search worked
#
#
#  Scenario: User can search for a product on target
#    Given Open target main page
#    When Search for coffee
#    Then Verify search worked

Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <search_text>
    Then Verify search worked for <expected_result>
    Examples:
    | search_text | expected_result |
    | tea         | tea             |
    | mug         | mug              |
    | coffee      | coffee          |