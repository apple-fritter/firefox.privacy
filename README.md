# Firefox Privacy and Security Settings
This program sets the privacy and security settings for Firefox to be more privacy-focused, and removes extraneous data from the settings.ini file. Additionally, it sets Firefox to run in incognito mode only.

## Requirements
* Python 3.x
* Firefox web browser
## Usage
Clone this repository to your local machine.
Open a command prompt and navigate to the directory containing the firefox_settings.py file.
Run the following command to execute the program:
bash
Copy code
```python firefox_settings.py```
When prompted, enter the path to your Firefox profile directory. This directory is usually located in the following directories:

Windows: %APPDATA%\Mozilla\Firefox\Profiles

macOS: ~/Library/Application Support/Firefox/Profiles

Linux: ~/.mozilla/firefox

The program will update the settings.ini file with the desired privacy and security settings, and set Firefox to run in incognito mode only.
Privacy and Security Settings
The program sets the following privacy and security settings:
#### python
```
settings = {
    "privacy.clearOnShutdown.cache": "true",
    "privacy.clearOnShutdown.cookies": "true",
    "privacy.clearOnShutdown.downloads": "true",
    "privacy.clearOnShutdown.formdata": "true",
    "privacy.clearOnShutdown.history": "true",
    "privacy.clearOnShutdown.offlineApps": "true",
    "privacy.clearOnShutdown.sessions": "true",
    "privacy.donottrackheader.enabled": "true",
    "privacy.firstparty.isolate": "true",
    "privacy.trackingprotection.enabled": "true",
    "privacy.trackingprotection.socialtracking.enabled": "true",
    "network.cookie.cookieBehavior": "1",
    "network.cookie.thirdparty.sessionOnly": "true",
    "network.cookie.lifetimePolicy": "2",
    "browser.cache.disk.enable": "false",
    "browser.cache.memory.enable": "false",
    "browser.cache.offline.enable": "false",
    "browser.safebrowsing.malware.enabled": "true",
    "browser.safebrowsing.phishing.enabled": "true",
    "browser.safebrowsing.downloads.enabled": "true",
    "browser.safebrowsing.downloads.remote.enabled": "true",
    "browser.safebrowsing.provider.mozilla.updateURL": "https://safebrowsing.mozilla.org/update?version=%VERSION%&appver=%APP_VERSION%&pver=2.2",
    "browser.safebrowsing.provider.mozilla.gethashURL": "https://safebrowsing.mozilla.org/gethash?client=firefox&appver=%APP_VERSION%&pver=2.2&keyver=%KEY_VERSION%",
}
```
Contributing
If you have any suggestions or improvements, feel free to open a pull request or create an issue.
