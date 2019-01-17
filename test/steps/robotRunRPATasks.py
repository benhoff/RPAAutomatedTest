from actor import Actor
from abilities.defaultAbilities import runRPATask
from tasks.defaultTasks import run

@given(u'Robot runs {task}')
def step_impl(context,task):
    context.Robot=Actor(named='BotMarley')
    context.Robot.can(runRPATask)
    context.Robot.wasAbleTo(
        run(The=task)
    )