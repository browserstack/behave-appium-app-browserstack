import time
from appium.webdriver.common.mobileby import MobileBy
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
