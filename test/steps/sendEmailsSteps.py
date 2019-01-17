from tasks.customTasks import sendTheEmail
from questions.sendEmailsQuestions import renameAllTempFiles

@when(u'Robot send email with: {theData}')
def step_impl(context, theData):
    context.Robot.attemptsTo(
        sendTheEmail,With=theData
    )

@then(u'the Robot should have marked all temporary files as {state}')
def step_impl(context,state):
    context.Robot.should(
        renameAllTempFiles,to=state
    )