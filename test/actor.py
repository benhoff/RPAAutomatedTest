import sys
sys.path.append("..")
from testConfig import config
sys.path.append(config['BASE_DIR'])

class Actor(object):
    def __init__(self,named,**kwargs):
        sys.path.append(config['BASE_DIR'])
        self.named=named
        self.systemUnderTest=None


    def attemptsTo(self,*args,**kwargs):
        self.performs(*args,**kwargs)
    def wasAbleTo(self,*args,**kwargs):
        self.performs(*args,**kwargs)
    def shouldSee(self,*args,**kwargs):
        self.performs(*args,**kwargs)
        self.finish()

    def can(self,Ability,*args,**kwargs):
        execute=Ability(**kwargs)
        if execute: self.systemUnderTest=execute

    def performs(self,*args,**kwargs):
        for arg in args:
            execute=arg(self.systemUnderTest,**kwargs)
    
    def finish(self,*args,**kwargs):
        self.systemUnderTest.close()
    
if __name__=='__main__':
    pass
