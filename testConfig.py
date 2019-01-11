import os
import getpass

# config = {
#     'BASE_DIR':os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
#     'RPA_TOOl':'UIPath',
#     'LOG_PATH':f'C:\\Users\\{getpass.getuser()}\\AppData\\Local\\UiPath\\Logs\\',
#     'RPA_TASK_FOLDER':f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}\\',
#     'TEST_RESULTS_FOLDER': ['']
# }

config = {
    'BASE_DIR':os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'RPA_TOOl':'AutomationAnywhere',
    'AA_TASK_NAME':'Office365Loggin',
    'LOG_PATH':f'C:\\Users\\{getpass.getuser()}\\Documents\\Automation Anywhere Files\\Automation Anywhere\\My Tasks\\DAPI Template AA2\\N00XX\\1.O365Login\\Logs\\',
    'RPA_TASK_FOLDER':f'C:\\Users\\{getpass.getuser()}\\Documents\\Automation Anywhere Files\\Automation Anywhere\\My Tasks\\DAPI Template AA2\\N00XX\\1.O365Login\\',
    'TEST_RESULTS_FOLDER': ['']
}


if __name__=="__main__":
    pass
    print(config['BASE_DIR'])
