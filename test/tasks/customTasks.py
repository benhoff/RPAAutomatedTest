from interactions.defaultInteractions import tailAndWaitFor
from logDriver import LogDriver


def sendTheEmail(log: LogDriver, **kwargs) -> LogDriver:
    tailAndWaitFor(log, kwargs['With'])


def changeThe(log: LogDriver, **kwargs) -> LogDriver:
    tailAndWaitFor(log, kwargs['Row'])


def andDelete(log: LogDriver, **kwargs) -> LogDriver:
    tailAndWaitFor(log, kwargs['The'])