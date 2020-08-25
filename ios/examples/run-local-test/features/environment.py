from appium import webdriver
from browserstack.local import Local
import os, json

config_file_path = os.path.join(os.path.dirname(__file__), '..', "config.json")
print("Path to the config file = %s" % (config_file_path))
with open(config_file_path) as config_file:
    CONFIG = json.load(config_file)

# Take user credentials from environment variables if they are defined
if 'BROWSERSTACK_USERNAME' in os.environ: CONFIG['capabilities']['browserstack.user'] = os.environ['BROWSERSTACK_USERNAME'] 
if 'BROWSERSTACK_ACCESS_KEY' in os.environ: CONFIG['capabilities']['browserstack.key'] = os.environ['BROWSERSTACK_ACCESS_KEY']

def start_local():
    """Starts BrowserStack local"""
    global bs_local
    bs_local = Local()
    bs_local_args = { "key": CONFIG['capabilities']['browserstack.key'], "forcelocal": "true" }
    bs_local.start(**bs_local_args)

def stop_local():
    """Stops BrowserStack local"""
    global bs_local
    if bs_local is not None:
        bs_local.stop()

def before_all(context):
    # Start BrowserStack Local before start of the test suite
    start_local()

def before_feature(context, feature):
    desired_capabilities = CONFIG['capabilities']
    context.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://hub-cloud.browserstack.com/wd/hub"
    )

def after_feature(context, feature):
    # Invoke driver.quit() after the test is done to indicate to BrowserStack 
    # that the test is completed. Otherwise, test will appear as timed out on BrowserStack.
    context.browser.quit()

def after_all(context):
    # Stop BrowserStack Local after end of the test suite
    stop_local()