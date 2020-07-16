# Test for BrowserStack's sample local iOS app.
# Note: If you have uploaded your app to BrowserStack update the test here.

Feature: BrowserStack Local Testing
    Scenario: can check tunnel working
        Given I open app and click on button
        Then page contains "Up and running"
