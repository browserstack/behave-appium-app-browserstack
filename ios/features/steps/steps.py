import time
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I open the app and click on Text Button')
def step_impl(context):
    element = WebDriverWait(context.browser, 30).until(
        EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Text Button"))
    )
    element.click()


@then(u'Type "{text}" and hit enter')
def step_impl(context, text):
    text_input = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Text Input"))
    )
    text_input.send_keys(text+"\n")
    time.sleep(5)
    
@then(u'Verify displayed text matches input text')
def step_impl(context):
    text_output = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Text Output"))
    )
    if text_output!=None and text_output.text=="hello@browserstack.com":
        assert True
    else:
        assert False

def existence_lambda(s):
    result = s.find_element(AppiumBy.ACCESSIBILITY_ID, "ResultBrowserStackLocal").get_attribute("value")
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
    result_element = context.browser.find_element(AppiumBy.ACCESSIBILITY_ID, "ResultBrowserStackLocal")
    result_string = result_element.text.lower()

    if result_string.__contains__("not working"):
        screenshot_file = "%s/screenshot.png" % os.getcwd()
        context.browser.save_screenshot(screenshot_file)
        print("Screenshot stored at %s" % (screenshot_file))
        raise Exception("Unexpected BrowserStackLocal test result")
    else:
        assert(result_string.__contains__(regex.lower()))
