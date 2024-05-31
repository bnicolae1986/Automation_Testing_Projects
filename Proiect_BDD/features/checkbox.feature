Feature:  all tests for checkboxes

@checkbox @select
Scenario: Select the first checkbox
  Given I am on the checkbox page
  When I click on the first checkbox
  Then The checkbox is selected

@checkbox @unselect
Scenario: Unselect the second checkbox
  Given I am on the checkbox page
  When I click on the second checkbox
  Then The checkbox is unselected
