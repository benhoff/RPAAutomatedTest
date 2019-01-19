from tasks.defaultTasks import executeThe
from questions.excelReaderQuestions import haveCreated
from behave import when, then


@when(u'Robot read the row until get the data: {last}')
def step_impl_read_the_row(context, last):
    context.Robot.attemptsTo(
        executeThe, Process=last
    )


@then(u'Robot creates {n} files in tempData')
def step_impl_creates_n_files(context, n):
    context.Robot.should(
        haveCreated, Files=n
    )