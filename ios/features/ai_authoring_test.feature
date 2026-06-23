# Test using AI Agent commands
Feature: AI Authoring Search Functionality
    Scenario: Search using AI Agent
        Given I search using AI Agent for keyword "BrowserStack"
        Then AI Agent verifies search results are displayed
