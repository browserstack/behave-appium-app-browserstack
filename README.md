# behave-appium-app-browserstack

This repository demonstrates how to run Appium Behave tests on BrowserStack App Automate using SDK.

### Requirements

* Python3

## Setup

* Clone the repo with `git clone -b sdk https://github.com/browserstack/pytest-appium-app-browserstack.git`
* It is recommended to use a virtual environment to install dependencies. To create a virtual environment:
  ```
  python3 -m venv env
  source env/bin/activate # on Mac
  env\Scripts\activate # on Windows
  ```
* Install dependencies `pip install -r requirements.txt`
* To run your automated tests using BrowserStack, you must provide a valid username and access key. This can be done either by providing your username and access key in the `browserstack.yml` configuration file, or by setting the `BROWSERSTACK_USERNAME` and `BROWSERSTACK_ACCESS_KEY` environment variables.

## Getting Started

Getting Started with Appium tests in Behave on real BrowserStack couldn't be easier!

### **Run first test :**

**1. Upload your Android or iOS App**

Specify your Android app (.apk or .aab file) or iOS app (.ipa file) in the `browserstack.yml` configuration file. Here is an example app config :

```
app: '/path/to/local/app.apk'
```

Set `app` to use the appliction under test for Appium sessions. Available options: app: `/path/to/local/app.apk` OR app: `bs://<app-id>` i.e App URL returned when uploading the app to BrowserStack manually. Visit https://www.browserstack.com/docs/app-automate/appium/set-up-tests/specify-app for more options

**Note**: If you do not have an .apk or .ipa file and are looking to simply try App Automate, you can download and test using our [sample Android app](https://www.browserstack.com/app-automate/sample-apps/android/WikipediaSample.apk) or [sample iOS app](https://www.browserstack.com/app-automate/sample-apps/ios/BStackSampleApp.ipa).

**2. Configure and run your first single test**

Open `browserstack.yml` file in `android` folder for Android and `ios` folder for iOS:

- Replace `YOUR_USERNAME` & `YOUR_ACCESS_KEY` in the `browserstack.yml` configuration file. Get your BrowserStack access credentials from [here](https://www.browserstack.com/accounts/settings)

- Replace `app: bs://<app-id>` with the URL obtained from app upload step or mention the path to your apk file.

- Run the below command to execute a Android test on BrowserStack AppAutomate:
    ```
    cd android
    browserstack-sdk behave features/first_test.feature
    ```

- Run the below command to execute a iOS test on BrowserStack AppAutomate:
    ```
    cd ios
    browserstack-sdk behave features/first_test.feature
    ```

- You can access the test execution results, and debugging information such as video recording, network logs on [App Automate dashboard](https://app-automate.browserstack.com/dashboard)

### **Use Local testing for apps that access resources hosted in development or testing environments :**

Open `browserstack.yml` file in `android` folder for Android and `ios` folder for iOS:

- Replace `YOUR_USERNAME` & `YOUR_ACCESS_KEY` in the `browserstack.yml` configuration file. Get your BrowserStack access credentials from [here](https://www.browserstack.com/accounts/settings)

- Replace `app: bs://<app-id>` with the URL obtained from app upload step or mention the path to your apk file.

- Run the below command to execute a Android test on BrowserStack AppAutomate:
    ```
    cd android
    browserstack-sdk behave features/first_test.feature
    ```

- Run the below command to execute a iOS test on BrowserStack AppAutomate:
    ```
    cd ios
    browserstack-sdk behave features/first_test.feature
    ```

- You can access the test execution results, and debugging information such as video recording, network logs on [App Automate dashboard](https://app-automate.browserstack.com/dashboard)

**Note**: If you are facing any issues, refer [Getting Help section](#Getting-Help)

## Integration with other python frameworks

For other Python frameworks samples, refer to following repositories :

- [Lettuce](https://github.com/browserstack/lettuce-appium-app-browserstack)
- [Python Native](https://github.com/browserstack/python-appium-app-browserstack)

Note: For other test frameworks supported by App-Automate refer our [Developer documentation](https://www.browserstack.com/docs/)

## Getting Help

If you are running into any issues or have any queries, please check [Browserstack Support page](https://www.browserstack.com/support/app-automate) or [get in touch with us](https://www.browserstack.com/contact?ref=help).
