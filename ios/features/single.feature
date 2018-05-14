Feature: 
    Scenario: Displayed Text should match Input Text
        Given I open the app and click on Text Button
        Then Type "hello@browserstack.com" and hit enter
        Then Verify displayed text matches input text
