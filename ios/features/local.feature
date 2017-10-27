Feature: BrowserStack Local Testing
    Scenario: can check tunnel working
        Given I open app and click on button
        Then page contains "Up and running"
