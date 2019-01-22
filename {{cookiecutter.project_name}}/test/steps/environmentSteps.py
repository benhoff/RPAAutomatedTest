from utils.fileUtils import deleteFiles
from utils.fileUtils import copyFiles
from utils.fileUtils import copyFile
from testConfig import config
from behave import given


@given(u'All the residual files have been deleted')
def step_impl_delete_residual_files(context):
    deleteFiles(
        PathDirectory=f'{config["RPA_TASK_FOLDER"]}Temps//',
        Pattern='*.txt'
    )


@given(u'is {testdata} in the temp folder')
def step_impl_copy_test_data_folder(context, testdata):
    testResourcesDir = config['TEST_RESOURCES_FOLDER']
    copyFiles(
        srcFolder=f'{config["BASE_DIR"]}{testResourcesDir}{testdata}//',
        dstFolder=f'{config["RPA_TASK_FOLDER"]}Temps//'
    )


@given(u'is {testdatafile} in the input folder named as {filename}')
def step_impl_copy_test_data_file(context, testdatafile, filename):
    testResourcesDir = config['TEST_RESOURCES_FOLDER']
    copyFile(
        srcFile=f'{config["BASE_DIR"]}{testResourcesDir}{testdatafile}',
        dstFile=f'{config["RPA_TASK_FOLDER"]}//Inputs//{filename}'
    )
