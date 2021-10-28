# Created by annakarelina at 10/27/21
Feature: Test Scenario for Add Movie functionality
# Enter feature name here
  # Enter feature description here

  Scenario Outline: User can add movie to the catalogue
    Given Open Add Movie page
    When Input valid Title into title field
    And Input valid <data> into data field
    And Input valid <number> into rating field
    Then Message Movie has been successfully added to the catalogue is shown
    Examples:
      |data      |number|
      |10/26/2021| 1    |
      |01/10/2015| 5    |

  Scenario Outline: User can not add movie with invalid input
    Given Open Add Movie page
    When Input invalid title ----- into title field
    And Input invalid <data> into data field
    And Input invalid <number> into rating field
    Then Error message Provide a valid input is shown
    Examples:
      |data      |number|
      |10/35/2000| -1   |
      |01/09/2015| 6    |
