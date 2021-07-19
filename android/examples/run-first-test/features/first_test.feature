Feature: POC for Appium-behave-BrowserStack
    Scenario: Should increment click counter when button is clicked
        Given I open the app
        When I click the button "Click me"
        Then I should see the text "You clicked 1 times"