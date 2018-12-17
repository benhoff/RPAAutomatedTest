from glob import glob
from testConfig import config
import os

def deleteFiles(PathDirectory,Pattern):
    CSVFiles=glob(f'{config[PathDirectory][0]}\\{Pattern}')
    for File in CSVFiles:
        os.remove(File)