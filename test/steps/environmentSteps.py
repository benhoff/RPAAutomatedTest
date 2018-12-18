from utils.fileUtils import deleteFiles

@given(u'All the residual files have been deleted')
def step_impl(context):
    deleteFiles('TEST_RESULTS_FOLDER','*.CSV')