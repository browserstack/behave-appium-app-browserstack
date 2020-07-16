Feature: Wikipedia Search Functionality
    Scenario: can find search results
        Given I open the app and search for keyword "BrowserStack"
        Then Search results should appear
