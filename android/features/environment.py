from appium import webdriver

def before_feature(context, feature):
    desired_capabilities = {
        'browserName': 'chrome'
    }
    context.browser = webdriver.Remote( desired_capabilities=desired_capabilities,command_executor="https://hub.browserstack.com/wd/hub")


def after_feature(context, feature):
    # Invoke driver.quit() after the test is done to indicate to BrowserStack 
    # that the test is completed. Otherwise, test will appear as timed out on BrowserStack.
    context.browser.quit()
