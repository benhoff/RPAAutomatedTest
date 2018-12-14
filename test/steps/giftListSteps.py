import sys
sys.path.append("..")
from actor import Actor
from abilities.customAbilities import runRPATask
from tasks.customTasks import run
from tasks.customTasks import executeThe

Robot=None

@given(u'Robot runs {task} in {RPATool}')
def step_impl(context,task,RPATool):
    global Robot
    Robot=Actor(named='BotMarley')
    Robot.can(runRPATask)
    Robot.wasAbleTo(
        run(The=task)
    )

@when(u'Robot do the {current} process')
def step_impl(context,current):

    Robot.attemptsTo(
        executeThe,Process=current
    )

@then(u'All the process should be in {one} state')
def step_impl(context,one):
    
    Robot.shouldFinish(
        inState=one
        )

    # raise NotImplementedError(u'STEP: Then The test should stop')