import sys
import os
sys.path.append("..")
from testConfig import config
import distutils.spawn
import getpass
from logDriver import LogDriver

def is_tool(name):
    return distutils.spawn.find_executable(name) is not None

def runRPATask(**usingAndLogginIn): 
    deafultRPATool=config['RPA_TOOl']
    logFilePath=config['LOG_PATH']
    sys.path.append(config['BASE_DIR'])
    try:
        if usingAndLogginIn['using'] and usingAndLogginIn['andLogginIn']:
            deafultRPATool=usingAndLogginIn['using']
            logFilePath=usingAndLogginIn['andLogginIn']
    except KeyError:
        pass
    if 'uipath' in deafultRPATool.lower():
        if is_tool(f'C:\\Users\\{getpass.getuser()}\\AppData\\Local\\UiPath\\UiPath.Agent.exe') and os.path.isdir(logFilePath):
            return LogDriver

    raise Exception('Check RPATool or log folder')


if __name__=='__main__':
    runRPATask()
