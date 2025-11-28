Feature: User Login
  As a registered user
  I want to log in
  so I can access my tasks

  Background: 
    Given a registered user exists

  Scenario: Successful login with correct credentials    
    Given I am on the login page
    When I enter valid credentials
    Then I should be redirected to the homepage  

  Scenario: Login fails with incorrect password
    Given I am on the login page
    When I enter an incorrect password
    Then I should remain on the login page 

  Scenario: Login fails with incorrect username
    Given I am on the login page
    When I enter an incorrect username
    Then I should remain on the login page 

  Scenario: Logged-in user cannot see the login page again
    Given I am already logged in
    When I try to visit the login page
    Then I should be redirected to the homepage 