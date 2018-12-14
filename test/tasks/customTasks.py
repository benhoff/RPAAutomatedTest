import os
from testConfig import config
import getpass
from glob import glob
from logDriver import LogDriver
from interactions.defaultInteractions import tailAndWaitFor 

def run(**kwargs):
    RPATaskFolder=config['RPA_TASK_FOLDER']
    task=kwargs['The']
    robotRunnerPath=glob(f'C:\\Users\\{getpass.getuser()}\\AppData\\Local\\UiPath\\app-*')[0]
    os.popen(f'{robotRunnerPath}\\UiRobot.exe /file:"{RPATaskFolder}{task}"')
    return LogDriver

def executeThe(log : LogDriver,**kwargs) -> LogDriver:
    tailAndWaitFor(log,kwargs['Process'])

if __name__=='__main__':
    writeOnSearchBar()