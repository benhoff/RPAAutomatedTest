import time
import datetime
from testConfig import config

class LogDriver(object):
    def __init__(self,*args,**kwargs):
        pass

    def todayExecutionLog(self,*args,**kwargs):
        return str(datetime.date.today())

    def follow(self,*args,**kwargs):
        thefile=open(f"{config['LOG_PATH']}{self.todayExecutionLog()}_Execution.log")
        thefile.seek(0,2)
        while True:
            line = thefile.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line
