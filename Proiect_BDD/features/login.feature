Feature: all login tests for the internet login page

 @login @negative
 Scenario: negative scenario
    Given I am on the login page
    When I insert an username "bogdan"
    When I insert a password "parola"
    When I click on the login button
    Then The message is "Your username is invalid!"

 @login @positive
 Scenario: positive scenario
    Given I am on the login page
    When I insert an username "tomsmith"
    When I insert a password "SuperSecretPassword!"
    When I click on the login button
    Then The message is "You logged into a secure area!"

 @logout
 Scenario: logout scenario
    Given I am on the login page
    When I insert an username "tomsmith"
    When I insert a password "SuperSecretPassword!"
    When I click on the login button
    Then The message is "You logged into a secure area!"
    When I click on the logout button
    Then The second message is "You logged out of the secure area!"

 @login @negative @negative2
 Scenario: negative scenario 2
    Given I am on the login page
    When I insert an username "bogdan"
    When I insert a password "SuperSecretPassword!"
    When I click on the login button
    Then The message is "Your username is invalid!"

  @login @negative @negative3
  Scenario: negative scenario 3
    Given I am on the login page
    When I insert an username "tomsmith"
    When I insert a password "parolagresita"
    When I click on the login button
    Then The message is "Your password is invalid!"

  @login @negative @negative4
  Scenario: negative scenario 4
    Given I am on the login page
    When I dont insert an username
    When I dont insert a password
    When I click on the login button
    Then The message is "Your username is invalid!"
