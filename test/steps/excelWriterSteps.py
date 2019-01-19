from tasks.customTasks import changeThe
from tasks.customTasks import andDelete
from questions.defaultQuestions import switchTheState
from behave import when, then


@when(u'Robot change row {n} and delete {file}')
def step_impl_change_row_and_delete_file(context, n, file):
    context.Robot.attemptsTo(
        changeThe, andDelete, Row=n, The=file
    )


@then(u'All the {column} in excel {file} should be {inState}')
def step_impl_check_for_excel_row(context, column, file, inState):
    context.Robot.should(
        switchTheState, of=column, In=file, to=inState
    )