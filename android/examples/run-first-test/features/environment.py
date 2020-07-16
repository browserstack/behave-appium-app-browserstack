from appium import webdriver
from browserstack.local import Local
import os, json

config_file_path = os.path.join(os.path.dirname(__file__), '..', "config.json")
print("Config file = %s" % (config_file_path))
with open(config_file_path) as config_file:
    CONFIG = json.load(config_file)

BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME'] if 'BROWSERSTACK_USERNAME' in os.environ else CONFIG['username']
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY'] if 'BROWSERSTACK_ACCESS_KEY' in os.environ else CONFIG['access_key']

def before_feature(context, feature):
    desired_capabilities = CONFIG['capabilities']
    context.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://%s:%s@hub-cloud.browserstack.com/wd/hub" % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY)
    )

def after_feature(context, feature):
    context.browser.quit()
