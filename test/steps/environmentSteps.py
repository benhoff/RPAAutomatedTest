from utils.fileUtils import deleteFiles
from utils.fileUtils import copyFiles
from testConfig import config

@given(u'All the residual files have been deleted')
def step_impl(context):
    deleteFiles(
        PathDirectory=f'{config["TEST_RESULTS_FOLDER"][0]}',
        Pattern='row*.txt'
    )

@given(u'is {testdata} in the temp folder')
def step_impl(context,testdata):
    copyFiles(
        srcFolder=f'{config["BASE_DIR"]}//RPAAutomatedTest//test//test_resources//{testdata}//', 
        dstFolder=f'{config["TEST_RESULTS_FOLDER"][0]}'
    )
