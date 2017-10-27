import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'I open the app and search for keyword "{keyword}"')
def step_impl(context, keyword):
    search_element = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Search Wikipedia"))
    )
    search_element.click()

    search_input = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "org.wikipedia.alpha:id/search_src_text"))
    )
    search_input.send_keys(keyword)
    time.sleep(5)


@then(u'Search results should appear')
def step_impl(context):
    elems = context.browser.find_elements_by_class_name("android.widget.TextView")
    assert len(elems) > 0, "results not populated"


# Local Steps
@given(u'I open app and click on button')
def step_impl(context):
    element = WebDriverWait(context.browser, 30).until(
        EC.presence_of_element_located((MobileBy.ID, "com.example.android.basicnetworking:id/test_action"))
    )
    element.click()
    WebDriverWait(context.browser, 30).until(
        EC.presence_of_element_located((MobileBy.CLASS_NAME, "android.widget.TextView"))
    )
        
@then(u'page contains "{regex}"')
def step_impl(context, regex):
    test_element = None
    search_results = context.browser.find_elements_by_class_name("android.widget.TextView")
    for result in search_results:
        if result.text.__contains__("The active connection is"):
            test_element = result

    if test_element is None:
        raise Exception("Cannot find the needed TextView element from app")

    matched_string = test_element.text
    assert matched_string.__contains__("The active connection is wifi"), "Incorrect Text"
    assert matched_string.__contains__("Up and running"), "Incorrect Text"
