Feature: User Login
  As a registered user
  I want to log in
  so I can access my tasks


  Scenario: Successful login with correct credentials
    Given a registered user exists
    And I am on the login page
    When I enter valid credentials
    Then I should be redirected to the homepage  