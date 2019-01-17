from tasks.defaultTasks import executeThe

@when(u'Robot do the: {current} process')
def step_impl(context,current):

    context.Robot.attemptsTo(
        executeThe,Process=current
    )

@then(u'Robot should: {getLogged}')
def step_impl(context,getLogged):
    context.Robot.attemptsTo(
        executeThe,Process=getLogged
    )   

