from utils.fileUtils import deleteFiles
from utils.fileUtils import copyFiles
from utils.fileUtils import copyFile
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

@given(u'is {testdatafile} in the input folder named as {filename}')
def step_impl(context,testdatafile,filename):
    copyFile(
        srcFile=f'{config["BASE_DIR"]}//RPAAutomatedTest//test//test_resources//testdata3//{testdatafile}', 
        dstFile=f'{config["RPA_TASK_FOLDER"]}//Inputs//{filename}'
    )
