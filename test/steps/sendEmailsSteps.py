from actor import Actor
from abilities.defaultAbilities import runRPATask
from tasks.defaultTasks import run
from tasks.customTasks import sendTheEmail
from questions.sendEmailsQuestions import renameAllTempFiles

# Robot = None

# @given(u'Robot runs {task}')
# def step_impl(context, task):
#     global Robot
#     Robot=Actor(named='BotMarley')
#     Robot.can(runRPATask)
#     Robot.wasAbleTo(
#         run(The=task)
#     )

@when(u'Robot send email with: {theData}')
def step_impl(context, theData):
    Robot.attemptsTo(
        sendTheEmail,With=theData
    )

@then(u'the Robot should have marked all temporary files as {state}')
def step_impl(context,state):
    Robot.should(
        renameAllTempFiles,to=state
    )