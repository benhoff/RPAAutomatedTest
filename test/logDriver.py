import time
import datetime
from testConfig import config
from collections import deque
import psutil

class LogDriver(object):
    #TODO: Remote Testing\SSH
    #TODO: Timeout\Optional
    def __init__(self,timeOut=None,*args,**kwargs):

        self.thefile=self.getLogFile()
        self.timeOut=None


    def getLogFile(self):
        if not config['AA_TASK_NAME']: config['AA_TASK_NAME'] = ''
        todayDate=time.strftime('%Y-%m-%d',time.strptime(self.todayDateExecutionLog(), '%Y-%m-%d'))
        for i in range(2):
            try:
                thefile=open(f"{config['LOG_PATH']}{todayDate}_{config['AA_TASK_NAME']}Execution.log")
            except FileNotFoundError:
                time.sleep(1)
                try:
                    thefile=open(f"{config['LOG_PATH']}{todayDate}_{config['AA_TASK_NAME']}Execution.log")
                except FileNotFoundError:
                    todayDate='-'.join( map( str, map(int,todayDate.split("-")) ) )    

        return thefile

    def todayDateExecutionLog(self,*args,**kwargs):
        return str(datetime.date.today())

    def follow(self,*args,**kwargs):
        self.thefile.seek(0,2)
        counter=0
        while True:
            line = self.thefile.readline()
            if not line:
                self.stopProcessByTimeOut(counter,self.timeOut)
                time.sleep(0.1)
                counter+=0.1
                continue
            yield line
        
    def getNLinesBeforeTheEnd(self,*args,**kwargs):
        time.sleep(1)
        return str(deque(self.thefile,maxlen=8))

    def close():
        pass

    def stopProcessByTimeOut(self,counter,timeOut,*args,**kwargs):
        #TODO: create am utils function for this 
        if self.timeOut:
            if counter>self.timeOut:
                for proc in psutil.process_iter():
                    if 'UiPath.Executor.exe' in str(proc):
                        proc.kill()
                        raise Exception(f'{self.timeOut}s Inactivity timeout Exception')


