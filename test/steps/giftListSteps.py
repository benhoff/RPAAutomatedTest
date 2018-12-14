import sys
sys.path.append("..")
from actor import Actor

Robot=None

@given(u'Robot runs {task} in {RPATool} and logs in {thefile}')
def step_impl(context,task,RPATool,thefile):
    global Robot
    Robot=Actor(named='BotMarley')
    Robot.can(runRPATask,using=RPATool,andLogginIn=thefile)
    Robot.wasAbleTo(
        run(The=task)
    )


@when(u'Robot do the {first} process')
def step_impl(context,first):
    # logfile = open("C:\\Users\\ryzen2600x\\Desktop\\python playground\\experimentacionextrema\\loggertest\\Overwatch.log","r")
    # loglines = follow(logfile)
    # for line in loglines:
    #     print (line)
    #     if 'hello' in line:
    #         return

    Robot.attemptsTo(
        executeThe,Process=first
    )

    # raise NotImplementedError(u'STEP: When The log stalker find hello fucking and world')

# @when(u'Robot do the {second} process')
# def step_impl(context,second):
#     Robot.attemptsTo(
#         executeThe,Process=second
#     )


# @when(u'Robot do the {third} process')
# def step_impl(context,third):
#     Robot.attemptsTo(
#         executeThe,Process=third
#     )

@then(u'All the process should be in {one} state')
def step_impl(context,one):
    
    Robot.shouldFinish(
        inState=one
        )

    # raise NotImplementedError(u'STEP: Then The test should stop')