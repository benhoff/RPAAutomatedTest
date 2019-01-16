from os.path import join
from testConfig import config
from glob import glob
from logDriver import LogDriver

def renameAllTempFiles(log : LogDriver,**kwargs):
    Files=glob(join(f'{config["TEST_RESULTS_FOLDER"][0]}','*.txt'))
    for file in Files:
        assert (kwargs['to'] in file)