import os
import sys
import distutils.spawn
import getpass
from logDriver import LogDriver
from testConfig import config


def is_tool(name):
    return distutils.spawn.find_executable(name) is not None


def runRPATask(**usingAndLogginIn):
    deafultRPATool = config['RPA_TOOl']
    logFilePath = config['LOG_PATH']
    sys.path.append(config['BASE_DIR'])
    if 'uipath' in deafultRPATool.lower():
        UserFolder = f'C:\\Users\\{getpass.getuser()}\\'
        UIAgent = f'{UserFolder}AppData\\Local\\UiPath\\UiPath.Agent.exe'
        if is_tool(UIAgent) and os.path.isdir(logFilePath):
            return LogDriver
    elif 'automationanywhere' in deafultRPATool.lower():
        AADir = 'C:\\Program Files (x86)\\Automation Anywhere'
        AA = f'{AADir}\\Enterprise\\Client\\Automation Anywhere.exe'
        if is_tool(AA) and os.path.isdir(logFilePath):
            return LogDriver
    raise Exception('Check RPATool or log folder')


