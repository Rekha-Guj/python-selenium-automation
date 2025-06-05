# Created by rekhagujalwar at 6/5/25
Feature: target user when logged out
  # a logged out user can navigate to Sign In

  Scenario: logged out user can navigate to Sign In

      Given Open target app main page
      When Clicked on Sign In
      Then Verify Sign In form is opened