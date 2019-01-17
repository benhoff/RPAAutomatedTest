from tasks.defaultTasks import executeThe
from questions.excelReaderQuestions import haveCreated

@when(u'Robot read the row until get the data: {last}')
def step_impl(context,last):
    context.Robot.attemptsTo(
        executeThe,Process=last
    )

@then(u'Robot creates {n} files in tempData')
def step_impl(context,n):
    context.Robot.should(
        haveCreated,Files=n
    )