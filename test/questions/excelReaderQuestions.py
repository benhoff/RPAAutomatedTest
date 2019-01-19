from glob import glob
from testConfig import config


def haveCreated(*args, **kwargs):
    filesCount = len(glob(f'{config["TEST_RESULTS_FOLDER"][0]}\\row_*.txt'))
    assert(filesCount == int(kwargs['Files']))