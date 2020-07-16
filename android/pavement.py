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
    packages=['android/examples/run-first-test/features', 'android/examples/run-local-test/features', 'android/examples/run-parallel-tests/features']
)

def run_behave_test(feature, task_id=0):
    if feature == 'first_test':
        sh('behave examples/run-first-test/features/first_test.feature')
    elif feature == 'local_test':
        sh('behave examples/run-local-test/features/local_test.feature')
    elif feature == 'parallel_tests':
        if platform.system() == 'Windows':
            sh('SET TASK_ID=%s & behave examples/run-parallel-tests/features/parallel_test.feature' % (task_id))
        else:
            sh('export TASK_ID=%s && behave examples/run-parallel-tests/features/parallel_test.feature' % (task_id))

@task
@consume_nargs(1)
def run(args):
    """Run first_test, local_test and parallel_tests using config files"""
    if args[0] == 'first_test':
        run_behave_test(args[0])
    elif args[0] == 'local_test':
        run_behave_test(args[0])
    elif args[0] == 'parallel_tests':
        jobs = []
        for i in range(4):
            p = threading.Thread(target=run_behave_test,args=(args[0],i))
            jobs.append(p)
            p.start()

        for thread in jobs:
            thread.join()
    else:
        print("Wrong paver task given") 

@task
def test():
    """Run all tests"""
    sh("paver run first_test")
    sh("paver run local_test")
    sh("paver run parallel_tests")
