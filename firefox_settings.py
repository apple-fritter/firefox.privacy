import configparser
import os

# Prompt the user for the path to the Firefox profile directory
profile_dir = input("Enter the path to your Firefox profile directory: ")

# Set the desired privacy and security settings
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

# Remove extraneous data from settings.ini
excluded_sections = ["General", "Profile", "Install Location", "Directories", "Compatibility"]
config = configparser.ConfigParser()
config.read(os.path.join(profile_dir, "settings.ini"))

for section in config.sections():
    if section not in excluded_sections:
        for option in config.options(section):
            if not (section in settings and option in settings[section]):
                config.remove_option(section, option)
        if not config.options(section):
            config.remove_section(section)

with open(os.path.join(profile_dir, "settings.ini"), "w") as configfile:
    config.write(configfile)

# Set Firefox to run in incognito mode only
with open(os.path.join(profile_dir, "user.js"), "w") as userjs:
    userjs.write('user_pref("browser.privatebrowsing.autostart", true);')

# Update the settings.ini file with the desired settings
config = configparser.ConfigParser()
config.read(os.path.join(profile_dir, "settings.ini"))

for section, options in settings.items():
    section_name, option_name = section.split(".", 1)
    if not config.has_section(section_name):
        config.add_section(section_name)
    config.set(section_name, option_name, options)

with open(os.path.join(profile_dir, "settings.ini"), "w") as configfile:
    config.write(configfile)

print("Firefox privacy and security settings updated.")
