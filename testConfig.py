import os

DEFAULT_DRIVER='/googleTranslateAutomatedTest/resources/drivers/chromedriver'

config = {
    'BASE_DIR':os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'DEFAULT_URL':'https://www.google.com/',
    'WEB_DRIVER': f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}{DEFAULT_DRIVER}',
    'DRIVER_OPTIONS_CONFIG': ['headless']
}

if __name__=="__main__":
    print(config['WEB_DRIVER'])
    #options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    #browser=webdriver.Chrome(desired_capabilities=DesiredCapabilities().CHROME,executable_path=r''+driverPath,chrome_options=options)
    # browser=webdriver.Chrome(desired_capabilities=DesiredCapabilities().CHROME,executable_path=r''+driverPath,chrome_options=options)
