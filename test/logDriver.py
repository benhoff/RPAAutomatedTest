import time
import datetime
from testConfig import config
from collections import deque

class LogDriver(object):
    #TODO: Remote Testing\SSH
    #TODO: Timeout\Optional
    def __init__(self,*args,**kwargs):
        try:
            self.thefile=open(f"{config['LOG_PATH']}{self.todayDateExecutionLog()}_Execution.log")
        except FileNotFoundError:
            time.sleep(5)
            self.thefile=open(f"{config['LOG_PATH']}{self.todayDateExecutionLog()}_Execution.log")

    def todayDateExecutionLog(self,*args,**kwargs):
        return str(datetime.date.today())

    def follow(self,*args,**kwargs):
        self.thefile.seek(0,2)
        while True:
            line = self.thefile.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line
        
    def getNLinesBeforeTheEnd(self,*args,**kwargs):
        time.sleep(1)
        return str(deque(self.thefile,maxlen=8))

    def close():
        pass


