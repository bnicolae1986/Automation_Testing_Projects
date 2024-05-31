Feature: all tests for alerts page

  @alerts
  Scenario: OK alert
    Given I am on the alerts page
    When I click on OK alert button
    When I accept alert
    Then The message for alerts page is "You successfully clicked an alert"

  @alerts
  Scenario: Dismiss alert - ok button
    Given I am on the alerts page
    When I click on Confirm alert button
    When I accept alert
    Then The message for alerts page is "You clicked: Ok"

  @alerts
  Scenario: Dismiss alert
    Given I am on the alerts page
    When I click on Confirm alert button
    When I dismiss alert
    Then The message for alerts page is "You clicked: Cancel"

  @alerts @prompt
  Scenario: Prompt alert
    Given I am on the alerts page
    When I click on Prompt alert button
    When I enter text "bogdan"
    When I accept alert
    Then The message displayed is "You entered: bogdan"

  @alerts @prompt @notext
  Scenario: Prompt alert no text
    Given I am on the alerts page
    When I click on Prompt alert button
    When I do not enter text
    When I accept alert
    Then The message3 displayed is "You entered:"


  @alerts @prompt @textcancel
  Scenario: Prompt alert text cancel
    Given I am on the alerts page
    When I click on Prompt alert button
    When I enter text "bogdan"
    When I dismiss alert
    Then The message4 displayed is "You entered: null"


  @alerts @prompt @notextcancel
  Scenario: Prompt alert notext cancel
    Given I am on the alerts page
    When I click on Prompt alert button
    When I do not enter text
    When I dismiss alert
    Then The message5 displayed is "You entered: null"















