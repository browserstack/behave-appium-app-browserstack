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
