from actor import Actor
from abilities.defaultAbilities import runRPATask
from tasks.defaultTasks import run
from behave import given


@given(u'Robot runs {task}')
def step_impl_robot_runs_rpa_task(context, task):
    context.Robot = Actor(named='BotMarley')
    context.Robot.can(runRPATask)
    context.Robot.wasAbleTo(
        run(The=task)
    )