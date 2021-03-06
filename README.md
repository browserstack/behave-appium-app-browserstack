# behave-appium-app-browserstack

This repository demonstrates how to run Appium Behave tests on BrowserStack App Automate.

## Setup

### Requirements

1. Python 3.6+ or Python 2.7+

    - If Python is not installed, follow these instructions:
        - For Windows, download latest python version from [here](https://www.python.org/downloads/windows/) and run the installer executable
        - For Mac and Linux, run `python --version` to see what python version is pre-installed. If you want a different version download from [here](https://www.python.org/downloads/)

2. Package Manager `pip`

    Note : `pip` comes installed with Python 2.7.9+ and python 3.4+

    - If `pip` is not installed, follow these instructions:
        - Securely download get-pip.py by following this link: [get-pip.py](https://bootstrap.pypa.io/get-pip.py) or use following cURL command to download it:

        ```sh
        curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        ```

        - After dowloading, run the file :

            - For Python 3

                ```sh
                python3 get-pip.py
                ```

            - For Python 2

                ```sh
                python2 get-pip.py
                ```

### Install the dependencies

To install the dependencies for Android tests, run :

- For Python 3

    ```sh
    pip3 install -r android/requirements.txt
    ```

- For Python 2

    ```sh
    pip2 install -r android/requirements.txt
    ```

Or,

To install the dependencies for iOS tests, run :

- For Python 3

    ```sh
    pip3 install -r ios/requirements.txt
    ```

- For Python 2

    ```sh
    pip2 install -r ios/requirements.txt
    ```

## Getting Started

Getting Started with Appium tests in Behave on real BrowserStack couldn't be easier!

### **Run first test :**

- Switch to `run-first-test` directory under [Android examples](android/examples/run-first-test) or [iOS examples](ios/examples/run-first-test)

- Follow the steps outlined in the documentation - [Get Started with your first test on App Automate](https://www.browserstack.com/docs/app-automate/appium/getting-started/python/behave)

### **Speed up test execution with parallel testing :**

- Switch to `run-prarallel-tests` directory under [Android examples](android/examples/run-parallel-tests) or [iOS examples](ios/examples/run-parallel-tests)

- Follow the steps outlined in the documentation - [Get Started with Parallel testing on App Automate](https://www.browserstack.com/docs/app-automate/appium/getting-started/python/behave/parallelize-tests)

### **Use Local testing for apps that access resources hosted in development or testing environments :**

- Switch to `run-local-test` directory under [Android examples](android/examples/run-local-test) or [iOS examples](ios/examples/run-local-test)

- Follow the steps outlined in the documentation - [Get Started with Local testing on App Automate](https://www.browserstack.com/docs/app-automate/appium/getting-started/python/behave/local-testing)

**Note**: If you are facing any issues, refer [Getting Help section](#Getting-Help)

## Integration with other python frameworks

For other Python frameworks samples, refer to following repositories :

- [Lettuce](https://github.com/browserstack/lettuce-appium-app-browserstack)
- [Python Native](https://github.com/browserstack/python-appium-app-browserstack)

Note: For other test frameworks supported by App-Automate refer our [Developer documentation](https://www.browserstack.com/docs/)

## Getting Help

If you are running into any issues or have any queries, please check [Browserstack Support page](https://www.browserstack.com/support/app-automate) or [get in touch with us](https://www.browserstack.com/contact?ref=help).
