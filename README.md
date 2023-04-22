# Firefox Privacy and Security Settings
This program sets the privacy and security settings for Firefox to be more privacy-focused, and removes extraneous data from the settings.ini file. Additionally, it sets Firefox to run in incognito mode only.

## Requirements
* Python 3.x
* Firefox web browser
## Usage
Clone this repository to your local machine.
Open a command prompt and navigate to the directory containing the firefox_settings.py file.
Run the following command to execute the program:
```python firefox_settings.py```

When prompted, enter the path to your Firefox profile directory. This directory is usually located in the following directories:

* Windows: %APPDATA%\Mozilla\Firefox\Profiles

* macOS: ~/Library/Application Support/Firefox/Profiles

* Linux: ~/.mozilla/firefox

## The program will update the settings.ini file
The program will update the settings.ini file with the desired privacy and security settings, and set Firefox to run in incognito mode only.
Privacy and Security Settings
The program sets the following privacy and security settings:
```
privacy.clearOnShutdown.cache to "true"
privacy.clearOnShutdown.cookies to "true"
privacy.clearOnShutdown.downloads to "true"
privacy.clearOnShutdown.formdata to "true"
privacy.clearOnShutdown.history to "true"
privacy.clearOnShutdown.offlineApps to "true"
privacy.clearOnShutdown.sessions to "true"
privacy.donottrackheader.enabled to "true"
privacy.firstparty.isolate to "true"
privacy.trackingprotection.enabled to "true"
privacy.trackingprotection.socialtracking.enabled to "true"
network.cookie.cookieBehavior to "1"
network.cookie.thirdparty.sessionOnly to "true"
network.cookie.lifetimePolicy to "2"
browser.cache.disk.enable to "false"
browser.cache.memory.enable to "false"
browser.cache.offline.enable to "false"
browser.safebrowsing.malware.enabled to "true"
browser.safebrowsing.phishing.enabled to "true"
browser.safebrowsing.downloads.enabled to "true"
browser.safebrowsing.downloads.remote.enabled to "true"
browser.safebrowsing.provider.mozilla.updateURL to "https://safebrowsing.mozilla.org/update?version=%VERSION%&appver=%APP_VERSION%&pver=2.2"
browser.safebrowsing.provider.mozilla.gethashURL to "https://safebrowsing.mozilla.org/gethash?client=firefox&appver=%APP_VERSION%&pver=2.2&keyver=%KEY_VERSION%"
```
## Contributing
If you have any suggestions or improvements, feel free to open a pull request or create an issue.

## [Disclaimer](DISCLAIMER)
**This software is provided "as is" and without warranty of any kind**, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

**The authors do not endorse or support any harmful or malicious activities** that may be carried out with the software. It is the user's responsibility to ensure that their use of the software complies with all applicable laws and regulations.

## License

These files released under the [MIT License](LICENSE).
