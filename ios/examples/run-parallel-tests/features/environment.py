from appium import webdriver
from browserstack.local import Local
import os, json

config_file_path = os.path.join(os.path.dirname(__file__), '..', "config.json")
print("Path to the config file = %s" % (config_file_path))
with open(config_file_path) as config_file:
    CONFIG = json.load(config_file)

TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0

# Take user credentials from environment variables if they are defined
if 'BROWSERSTACK_USERNAME' in os.environ: CONFIG['capabilities']['browserstack.user'] = os.environ['BROWSERSTACK_USERNAME'] 
if 'BROWSERSTACK_ACCESS_KEY' in os.environ: CONFIG['capabilities']['browserstack.key'] = os.environ['BROWSERSTACK_ACCESS_KEY']

def before_feature(context, feature):
    desired_capabilities = CONFIG['capabilities']
    desired_capabilities['device'] = CONFIG['environments'][TASK_ID]['device']
    context.browser = webdriver.Remote(
        desired_capabilities=dict(desired_capabilities),
        command_executor="http://hub-cloud.browserstack.com/wd/hub"
    )

def after_feature(context, feature):
    # Invoke driver.quit() after the test is done to indicate to BrowserStack 
    # that the test is completed. Otherwise, test will appear as timed out on BrowserStack.
    context.browser.quit()
