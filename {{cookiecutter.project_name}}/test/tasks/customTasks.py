from interactions.defaultInteractions import tailAndWaitFor
from logDriver import LogDriver


def changeThe(log: LogDriver, **kwargs) -> LogDriver:
    tailAndWaitFor(log, kwargs['Row'])
