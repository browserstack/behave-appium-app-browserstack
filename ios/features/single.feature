Feature: Wordpress Login
    Scenario: Non existing email should give error
        Given I open the app and click on login
        Then Enter email "hello@browserstack.com" and click on next
        Then Verify login error
