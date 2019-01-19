from logDriver import LogDriver


def tailAndWaitFor(log: LogDriver, theWord):
    loglines = log().follow()
    for line in loglines:
        # print(line)
        # print(theWord)
        # print(theWord in line)
        if theWord in line:
            return
        elif 'error' in line.lower():
            raise Exception(f'Error: {line}')
        elif 'Cannot communicate with the browser' in line:
            raise Exception(f'Test execution is stopped prematurely: {line}')


def tailNAndSearchFor(log: LogDriver, FinishConfirmation):
    nLinesBeforeTheEnd = log().getNLinesBeforeTheEnd()
    if FinishConfirmation in nLinesBeforeTheEnd:
        return
    else:
        raise Exception(f'Not finish confirmation in: {nLinesBeforeTheEnd}')