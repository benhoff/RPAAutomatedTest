from glob import glob
from testConfig import config

def haveCreated(*args,**kwargs):
    assert(len(glob(f'{config["TEST_RESULTS_FOLDER"][0]}\\row_*.txt'))==int(kwargs['Files']))