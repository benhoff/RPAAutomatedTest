from utils.fileUtils import deleteFiles
from utils.fileUtils import copyFiles
from utils.fileUtils import copyFile
from testConfig import config
from behave import given


@given(u'All the residual files have been deleted')
def step_impl_delete_residual_files(context):
    deleteFiles(
        PathDirectory=f'{config["TEST_RESULTS_FOLDER"][0]}',
        Pattern='row*.txt'
    )


@given(u'is {testdata} in the temp folder')
def step_impl_copy_test_data_folder(context, testdata):
    testResourcesDir = "//RPAAutomatedTest//test//test_resources//"
    copyFiles(
        srcFolder=f'{config["BASE_DIR"]}{testResourcesDir}{testdata}//',
        dstFolder=f'{config["TEST_RESULTS_FOLDER"][0]}'
    )


@given(u'is {testdatafile} in the input folder named as {filename}')
def step_impl_copy_test_data_file(context, testdatafile, filename):
    testDataDir = "//RPAAutomatedTest//test//test_resources//testdata3//"
    copyFile(
        srcFile=f'{config["BASE_DIR"]}{testDataDir}{testdatafile}',
        dstFile=f'{config["RPA_TASK_FOLDER"]}//Inputs//{filename}'
    )
