from tasks.defaultTasks import openBrowser
import sys
sys.path.append("..")
from testConfig import config

def runRPATask(**usingAndLogginIn):
    deafultUrl=config['DEFAULT_URL']
    webDriverPath=config['WEB_DRIVER']
    driverOptions=config['DRIVER_OPTIONS_CONFIG']

    sys.path.append(config['BASE_DIR'])

    try:
        if withBrowser['withBrowser']:
            return openBrowser(withBrowser.pop('withBrowser', ''),deafultUrl,driverOptions)
    except KeyError:
        pass
    return openBrowser(webDriverPath,deafultUrl,driverOptions)