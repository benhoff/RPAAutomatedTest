from testConfig import config
defaultDriver=config['WEB_DRIVER']

FIREFOX=f'{defaultDriver.split("drivers/")[0]}drivers/geckodriver'
CHROME=f'{defaultDriver.split("drivers/")[0]}drivers/chromedriver'

