Feature: Breaking gherkin reformatter

  Scenario Outline:
    Given I want to cause a bug
    When I try to reformat with an example table with a message like <message>
    Then gherkin reformatter explodes

    Examples:
      | message                 |
      | a\| b\n c\r d\t e\r\n f |
