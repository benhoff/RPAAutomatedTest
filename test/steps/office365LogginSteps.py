from actor import Actor
from abilities.defaultAbilities import runRPATask
from tasks.defaultTasks import run
from tasks.defaultTasks import executeThe

Robot=None

@given(u'Robot runs {task} for {File}')
def step_impl(context,task,File):
    global Robot
    Robot=Actor(named='BotMarley')
    Robot.can(runRPATask)
    Robot.wasAbleTo(
        run(The=task)
    )

@when(u'Robot do the: {current} process')
def step_impl(context,current):

    Robot.attemptsTo(
        executeThe,Process=current
    )

@then(u'Robot should: {getLogged}')
def step_impl(context,getLogged):
    Robot.attemptsTo(
        executeThe,Process=getLogged
    )   

