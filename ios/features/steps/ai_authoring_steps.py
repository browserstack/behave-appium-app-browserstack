from behave import given, then


@given('I search using AI Agent for keyword "{keyword}"')
def search_with_ai_agent(context, keyword):
    context.driver.execute_script(
        'browserstack_executor: {"action": "ai", "arguments": ["Tap on Search Wikipedia"]}'
    )
    context.driver.execute_script(
        f'browserstack_executor: {{"action": "ai", "arguments": ["Type {keyword} in the search field"]}}'
    )


@then('AI Agent verifies search results are displayed')
def verify_results_with_ai(context):
    context.driver.execute_script(
        'browserstack_executor: {"action": "ai", "arguments": ["Verify search results are displayed"]}'
    )
