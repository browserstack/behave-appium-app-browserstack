import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def existence_lambda(s):
    result = s.find_element_by_accessibility_id("ResultBrowserStackLocal").get_attribute("value")
    return result and len(result) > 0

@given(u'I open app and click on button')
def step_impl(context):
    test_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "TestBrowserStackLocal"))
    )
    test_button.click()


@then(u'page contains "{regex}"')
def step_impl(context, regex):
    WebDriverWait(context.browser, 30).until(existence_lambda)
    result_element = context.browser.find_element_by_accessibility_id("ResultBrowserStackLocal")
    result_string = result_element.text.lower()

    if result_string.__contains__("not working"):
        screenshot_file = "%s/screenshot.png" % os.getcwd()
        context.browser.save_screenshot(screenshot_file)
        print("Screenshot stored at %s" % (screenshot_file))
        raise Exception("Unexpected BrowserStackLocal test result")
    else:
        assert(result_string.__contains__(regex.lower()))