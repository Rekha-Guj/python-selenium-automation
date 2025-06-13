# Created by rekhagujalwar at 6/4/25 ---> HW_3

Feature: Amazon account creation
  # creating a user account at Amazon

  Scenario: User can create an account at Amazon web app
    Given Open Amazon account creation page
    When User details are entered
    Then Verify account is created and user is logged to Amazon app