import time
from logDriver import LogDriver

def tailAndWaitFor(log : LogDriver, theWord):
    # loglines=follow()
    loglines=log().follow()

    for line in loglines:
        if theWord in line:
            return
        elif 'execution ended' in line: raise Exception(f'Test execution is stopped prematurely: {line}')
        elif 'Error {"message":' in line: raise Exception(f'Error: {line}')