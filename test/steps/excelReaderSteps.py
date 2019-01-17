from actor import Actor
from abilities.defaultAbilities import runRPATask
from tasks.defaultTasks import run
from tasks.defaultTasks import executeThe
from questions.excelReaderQuestions import haveCreated

Robot=None

@given(u'Robot runs the {task} for {File}')
def step_impl(context,task,File):
    global Robot
    Robot=Actor(named='BotMarley')
    Robot.can(runRPATask)
    Robot.wasAbleTo(
        run(The=task)
    )

@when(u'Robot read the row until get the data: {last}')
def step_impl(context,last):
    Robot.attemptsTo(
        executeThe,Process=last
    )

@then(u'Robot creates {n} files in tempData')
def step_impl(context,n):
    Robot.should(
        haveCreated,Files=n
    )