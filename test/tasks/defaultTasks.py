import os
import getpass
from glob import glob
from testConfig import config
from logDriver import LogDriver
from interactions.defaultInteractions import tailAndWaitFor 
from interactions.defaultInteractions import tailNAndSearchFor

def argParser(kwargs):
    if kwargs: return f'{str(kwargs)}'


def run(The=None,withArgs=None,**kwargs):
    task=The
    deafultRPATool=config['RPA_TOOl']
    RPATaskFolder=config['RPA_TASK_FOLDER']

    if 'uipath' in deafultRPATool.lower():
        argx=argParser(withArgs)
        robotRunnerPath=glob(f'C:\\Users\\{getpass.getuser()}\\AppData\\Local\\UiPath\\app-*')[0]
        if argx: robotRunnerCommand=f'{robotRunnerPath}\\UiRobot.exe /file:"{RPATaskFolder}{task}" /input:"{argx}"'
        else: robotRunnerCommand=f'{robotRunnerPath}\\UiRobot.exe /file:"{RPATaskFolder}{task}"'
    elif 'automationanywhere' in deafultRPATool.lower(): robotRunnerCommand=f'{RPATaskFolder}{task}'
    
    os.popen(robotRunnerCommand)
    return LogDriver

def executeThe(log : LogDriver,**kwargs) -> LogDriver:
    tailAndWaitFor(log,kwargs['Process'])

def finishTheExecution(log: LogDriver, **kwargs) -> LogDriver:
    tailNAndSearchFor(log,kwargs['inState'])

if __name__=='__main__':
    pass


