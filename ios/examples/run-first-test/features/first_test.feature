# Test for BrowserStack's sample iOS app.
# Note: If you have uploaded your app to BrowserStack update the test here.
Feature: 
    Scenario: Displayed Text should match Input Text
        Given I open the app and click on Text Button
        Then Type "hello@browserstack.com" and hit enter
        Then Verify displayed text matches input text