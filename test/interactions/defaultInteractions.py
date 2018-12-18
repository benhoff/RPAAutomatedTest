import time

from logDriver import LogDriver

def tailAndWaitFor(log : LogDriver, theWord):
    loglines=log().follow()

    for line in loglines:
        if theWord in line:
            return
        elif 'execution ended' in line: raise Exception(f'Test execution is stopped prematurely: {line}')
        elif 'Error {"message":' in line: raise Exception(f'Error: {line}')
        
def tailNAndSearchFor(log: LogDriver, FinishConfirmation):
    nLinesBeforeTheEnd=log().getNLinesBeforeTheEnd()
    if FinishConfirmation in nLinesBeforeTheEnd:
        return
    else: raise Exception(f'Not finish confirmation in: {nLinesBeforeTheEnd}')