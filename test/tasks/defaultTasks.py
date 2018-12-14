from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


def openBrowser(driverPath,defaultUrl,driverOptions):
    options = Options()
    for option in driverOptions: options.add_argument(option)
    if 'geckodriver' in driverPath: browser=webdriver.Firefox(capabilities=DesiredCapabilities().FIREFOX,executable_path=r''+driverPath)
    elif 'chromedriver' in driverPath: browser=webdriver.Chrome(desired_capabilities=DesiredCapabilities().CHROME,executable_path=r''+driverPath,chrome_options=options)

    browser.get(defaultUrl)
    return browser


