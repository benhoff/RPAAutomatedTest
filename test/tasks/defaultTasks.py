import os
import getpass
from glob import glob
from testConfig import config
from logDriver import LogDriver
from interactions.defaultInteractions import tailAndWaitFor
from interactions.defaultInteractions import tailNAndSearchFor


def argParser(kwargs):
    if kwargs:
        return f'{str(kwargs)}'


def run(The=None, withArgs=None, **kwargs):
    task = The
    deafultRPATool = config['RPA_TOOl']
    RPATaskFolder = config['RPA_TASK_FOLDER']

    if 'uipath' in deafultRPATool.lower():
        argx = argParser(withArgs)
        robotRunnerPath = glob(
            f'C:\\Users\\{getpass.getuser()}\\AppData\\Local\\UiPath\\app-*'
        )[0]
        UiRobotExe = f'{robotRunnerPath}\\UiRobot.exe'
        xaml = f'/file:"{RPATaskFolder}{task}"'
        if argx:
            robotRunnerCommand = f'{UiRobotExe} {xaml} /input:"{argx}"'
        else:
            robotRunnerCommand = f'{UiRobotExe} {xaml}'
    elif 'automationanywhere' in deafultRPATool.lower():
        robotRunnerCommand = f'{RPATaskFolder}{task}'

    os.popen(f'"{robotRunnerCommand}"')

    return LogDriver


def executeThe(log: LogDriver, **kwargs) -> LogDriver:
    tailAndWaitFor(log, kwargs['Process'])


def finishTheExecution(log: LogDriver, **kwargs) -> LogDriver:
    tailNAndSearchFor(log, kwargs['inState'])



