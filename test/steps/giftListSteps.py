import sys
sys.path.append("..")
from actor import Actor
from abilities.customAbilities import runRPATask
from tasks.customTasks import run
from tasks.customTasks import executeThe
from tasks.customTasks import finishTheExecution
from questions.giftListRobotQuestions import amazonInformation
from questions.giftListRobotQuestions import ebayInformation
from utils.fileUtils import deleteFiles
from behave.model import Feature

Robot=None

def before_scenario(context,scenario):
    a=2/0
    deleteFiles('TEST_RESULTS_FOLDER','*.CSV')

@given(u'Robot runs {task} for {File} in {RPATool}')
def step_impl(context,task,RPATool,File):
    global Robot
    Robot=Actor(named='BotMarley')
    Robot.can(runRPATask)
    Robot.wasAbleTo(
        run(The=task,For=File)
    )

@when(u'Robot do the {current} process')
def step_impl(context,current):

    Robot.attemptsTo(
        executeThe,Process=current
    )

@then(u'All the process should be in {one} state')
def step_impl(context,one):
    
    Robot.should(
        finishTheExecution,inState=one
        )

@then(u'Robot should put the Amazon information in the CSV Files')
def step_impl(context):
    Robot.shouldSee(
        amazonInformation
    )

@then(u'Robot should put the Ebay information in the CSV Files')
def step_impl(context):
    Robot.shouldSee(
        ebayInformation
    )

def after_scenario(context, scenario):
    deleteFiles('TEST_RESULTS_FOLDER','*.CSV')

