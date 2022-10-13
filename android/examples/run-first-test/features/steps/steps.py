import time
from behave import *
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'I open the app')
def step_impl(context):
    pass

@when(u'I click the button "{buttonText}"')
def step_impl(context, buttonText):
    button = WebDriverWait(context.driver, 30).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.TextView[@text='"+buttonText+"']")))
    button.click()
    time.sleep(2)

@then(u'I should see the text "{textValue}"')
def step_impl(context, textValue):
    textEl = context.driver.find_element_by_xpath("//*[starts-with(@text,'You clicked')]")
    assert(textEl.text == textValue)