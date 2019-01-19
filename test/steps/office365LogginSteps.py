from tasks.defaultTasks import executeThe
from behave import when, then


@when(u'Robot do the: {current} process')
def step_impl_do_standard_process(context, current):
    context.Robot.attemptsTo(
        executeThe, Process=current
    )


@then(u'Robot should: {getLogged}')
def step_impl_should_do_process(context, getLogged):
    context.Robot.attemptsTo(
        executeThe, Process=getLogged
    )

