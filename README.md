# behave-appium-app-browserstack

This repository demonstrates how to run Appium automated mobile app tests using Behave framework on BrowserStack's real device cloud.

## Documentation

Refer  [Getting Started using Appium with Behave](https://www.browserstack.com/app-automate/appium-behave)

## Installation

### Requirements

1. Python 2.7+ or Python 3.5+

    - If Python is not installed, follow these instructions:
        - For Windows, download latest python version from [here](https://www.python.org/downloads/windows/) and run the installer exe
        - For Mac and Linux, run python --version to see what python version is pre-installed. If you want updated version download from [here](https://www.python.org/downloads/)

2. Pip

    - If pip is not installed, follow these instructions:
        - Securely download get-pip.py by following this link: [get-pip.py](https://bootstrap.pypa.io/get-pip.py) or use following curl command:

        ```sh
        curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        ```

        After downloading the file run :

        ```sh
        python get-pip.py
        ```

### Dependencies

- Depending on whether you are running android or iOS tests, run :

```sh
pip install -r android/requirements.txt or pip install -r ios/requirements.txt
```

## Getting Started

Getting Started with Appium mobile app tests using Behave on BrowserStack couldn't be easier!

### **Run first test in 3 simple steps :**

1. #### Upload App

    - Upload your android apk or iOS ipa file, or upload one of the Browserstack’s sample app [WikipediaSampleAndroidApp](https://www.browserstack.com/app-automate/sample-apps/android/WikipediaSample.apk) | [BStackSampleiOSApp](https://www.browserstack.com/app-automate/sample-apps/ios/BStackSampleApp.ipa)

        Note: Update username and accesskey with BrowserStack credentials (Find your BrowserStack credentials [here](https://www.browserstack.com/accounts/settings))

    ``` sh
    curl -u "username:accesskey" -X POST "https://api.browserstack.com/app-automate/upload" -F "file=@/path/to/app/file/Application-debug.apk"
    ```

    - Copy the 'app_url' (bs://\<hashed-app-id>) returned in the response and save it somewhere

2. #### Configure and run tests

    - Open single.json file in android/config folder to setup android tests or in ios/config folder to setup iOS tests

    - Update BrowserStack credentials by providing values to user & key variables in the opened file or set BROWSERSTACK_USERNAME & BROWSERSTACK_ACCESS_KEY environment variables (Find your BrowserStack credentials [here](https://www.browserstack.com/accounts/settings))

    - Update the desired_caps "app" capability with app_url (bs://\<hashed-app-id>) received in upload app API response

    - If you have uploaded your app instead of BrowserStack sample app, update the tests in the folders android/features or ios/features accordingly

    - Run tests with the following command inside android/ or ios/ folder

    ```sh
    paver run single
    ```

3. #### Thats it! view your tests results on [BrowserStack App Automate dashboard](https://app-automate.browserstack.com/)

    Note: If you face any issues, refer [Getting Help section](#Getting-Help)

### **Try BrowserStack parallel testing to speed up test execution**

1. #### Upload App

    - If you haven't already done, upload app as mentioned in the [Upload App section](#Upload-App)

2. #### Configure and run parallel tests

    - Open parallel.json file in android/config folder to setup android tests or in ios/config folder to setup iOS tests

    - Update BrowserStack credentials by providing values to user & key variables in the file or set BROWSERSTACK_USERNAME & BROWSERSTACK_ACCESS_KEY environment variables(Find your BrowserStack credentials [here](https://www.browserstack.com/accounts/settings))

    - Update the desired_caps "app" capability with app_url (bs://\<hashed-app-id>) received in upload app API response

    - If you have uploaded your app instead of BrowserStack sample app, update the tests in the folders android/features or ios/features accordingly

    - Run tests with following command inside android/ or ios/ folder

    ```sh
    paver run parallel
    ```

3. #### Thats it! view your tests results on [BrowserStack App Automate dashboard](https://app-automate.browserstack.com/)

    Note: If you face any issues, refer [Getting Help section](#Getting-Help)

### **Try BrowserStack Local Testing to test apps deployed on  development or testing environment**

1. #### Upload the app deployed on your internal environment

    - Upload your android app apk or iOS app ipa file, or upload one of the Browserstack’s sample app [LocalAndroidSample.apk](https://www.browserstack.com/app-automate/sample-apps/android/LocalSample.apk) | [LocaliOSSample.ipa](https://www.browserstack.com/app-automate/sample-apps/ios/LocalSample.ipa)

        Note: Update your BrowserStack credentials - username and accesskey (Find your BrowserStack credentials [here](https://www.browserstack.com/accounts/settings))

    ``` sh
    curl -u "username:accesskey" -X POST "https://api.browserstack.com/app-automate/upload" -F "file=@/path/to/app/file/Application-debug.apk"
    ```

    - Copy the 'app_url'(bs://\<hashed-app-id>) returned in the response and save it somewhere

2. #### Configure and run local tests

    - Open local.json file in android/config folder to setup android tests or in ios/config folder to setup iOS tests

    - Update BrowserStack credentials by providing values to user & key variables in the file or set BROWSERSTACK_USERNAME & BROWSERSTACK_ACCESS_KEY environment variables(Find your BrowserStack credentials [here](https://www.browserstack.com/accounts/settings))

    - Update the desired_caps "app" capability with app_url (bs://\<hashed-app-id>) received in upload app API response

    - If you have uploaded your app instead of BrowserStack sample app, update the tests in the folders android/features or ios/features accordingly

    - Run tests with following command inside android/ or ios/ folder

    ```sh
    paver run local
    ```

3. #### Thats it! View your tests results on [BrowserStack App Automate dashboard](https://app-automate.browserstack.com/)

    Note: If you face any issues, refer [Getting Help section](#Getting-Help)

## Integration with other python frameworks

For other Python frameworks samples, refer to following repositories :

- [Lettuce](https://github.com/browserstack/lettuce-appium-app-browserstack)
- [Appium Python Tests](https://github.com/browserstack/python-appium-app-browserstack)

Note: For other test frameworks supported by App-Automate refer [App-Automate testing frameworks documentation](https://www.browserstack.com/docs?product=app-automate)

## Getting Help

If you are running into any issues or have any queries, please check [Browserstack Support page](https://www.browserstack.com/support/app-automate) or [get in touch with us](https://www.browserstack.com/contact?ref=help).