from interactions.defaultInteractions import tailAndWaitFor
from logDriver import LogDriver

def sendTheEmail(log : LogDriver,**kwargs) -> LogDriver:
    tailAndWaitFor(log,kwargs['With'])