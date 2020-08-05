from paver.easy import *
from paver.setuputils import setup
import threading, os, platform

setup(
    name = "behave-browserstack",
    version = "0.1.0",
    author = "BrowserStack",
    author_email = "support@browserstack.com",
    description = ("Behave Integration with BrowserStack"),
    license = "MIT",
    keywords = "example appium browserstack",
    url = "https://github.com/browserstack/behave-appium-app-browserstack",
    packages =  ['features']
)

def run_behave_test(task_id=0):
    if platform.system() == 'Windows':
        sh('SET TASK_ID=%s & behave features/parallel_test.feature' % (task_id))
    else:
        sh('export TASK_ID=%s && behave features/parallel_test.feature' % (task_id))

@task
@consume_nargs(1)
def run(args):
    if args[0] == 'parallel_tests':
        jobs = []
        for i in range(2):
            p = threading.Thread(target=run_behave_test,args=(i,))
            jobs.append(p)
            p.start()

        for thread in jobs:
            thread.join()
    else:
        print("Wrong paver task given") 
