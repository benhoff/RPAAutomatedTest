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
        run(The=task,withArgs={'csvFileToRead':File})
    )

@when(u'Robot do the {current} process')
def step_impl(context,current):

    Robot.attemptsTo(
        executeThe,Process=current
    )

@then(u'Robot should {getLogged}')
def step_impl(context,getLogged):
    raise NotImplementedError(u'STEP: Then Robot should {getLogged}')

@then(u'the excel column status should be {loggedStatus}')
def step_impl(context,loggedStatus):
    raise NotImplementedError(u'STEP: Then the excel column status should be Logged')

