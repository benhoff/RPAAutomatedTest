import os
import getpass
from glob import glob
from testConfig import config
from logDriver import LogDriver
from interactions.defaultInteractions import tailAndWaitFor 
from interactions.defaultInteractions import tailNAndSearchFor

def run(**kwargs):
    task=kwargs['The']
    try:
        File=kwargs['For']
        argx = "{'csvFileToRead':'"+File+"'}"
    except KeyError:
        pass

    RPATaskFolder=config['RPA_TASK_FOLDER']
    robotRunnerPath=glob(f'C:\\Users\\{getpass.getuser()}\\AppData\\Local\\UiPath\\app-*')[0]
    if argx: os.popen(f'{robotRunnerPath}\\UiRobot.exe /file:"{RPATaskFolder}{task}" /input:"{argx}"')
    else: os.popen(f'{robotRunnerPath}\\UiRobot.exe /file:"{RPATaskFolder}{task}"')
    return LogDriver

def executeThe(log : LogDriver,**kwargs) -> LogDriver:
    tailAndWaitFor(log,kwargs['Process'])

def finishTheExecution(log: LogDriver, **kwargs) -> LogDriver:
    tailNAndSearchFor(log,kwargs['inState'])

if __name__=='__main__':
    pass