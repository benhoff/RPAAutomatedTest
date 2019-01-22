import os
import getpass

config = {
    'BASE_DIR':os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'RPA_TOOl':'{{cookiecutter.RPA_tool}}',
    'AA_TASK_NAME':'{{cookiecutter.RPA_task_name}}',
    'LOG_PATH':'{{cookiecutter.log_file_path}}',
    'RPA_TASK_FOLDER':'{{cookiecutter.Task_dir_folder}}',
    'TEST_RESOURCES_FOLDER':'\\{{cookiecutter.project_name}}{{cookiecutter.test_resources_dir_folder}}',
    'TEST_RESULTS_FOLDER': ['{{cookiecutter.robot_outputs_folder}}']
}


if __name__=="__main__":
    pass
    print(config['BASE_DIR'])
