# Test for BrowserStack sample Wikipedia Android app
# Note: If you have uploaded your app to BrowserStack update the test here
Feature: Wikipedia Search Functionality
    Scenario: can find search results
        Given I open the app and search for keyword "BrowserStack"
        Then Search results should appear
