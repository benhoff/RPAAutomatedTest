import os
import getpass

## UIPATH GiftListBot Config

# config = {
#     'BASE_DIR':os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
#     'RPA_TOOl':'UIPath',
#     'LOG_PATH':f'C:\\Users\\{getpass.getuser()}\\AppData\\Local\\UiPath\\Logs\\',
#     'RPA_TASK_FOLDER':f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}\\',
#     'TEST_RESULTS_FOLDER': ['']
# }

## AA 1.excelReader Config

# config = {
#     'BASE_DIR':os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
#     'RPA_TOOl':'AutomationAnywhere',
#     'AA_TASK_NAME':'1.excelReader',
#     'LOG_PATH':f'C:\\Users\\{getpass.getuser()}\\Documents\\Automation Anywhere Files\\Automation Anywhere\\My Tasks\\DAPI Template AA2\\N00XX\\1.O365Login\\Logs\\',
#     'RPA_TASK_FOLDER':f'C:\\Users\\{getpass.getuser()}\\Documents\\Automation Anywhere Files\\Automation Anywhere\\My Tasks\\DAPI Template AA2\\N00XX\\1.O365Login\\',
#     'TEST_RESULTS_FOLDER': ['C:\\Users\\juan.restrepo\\Documents\\Automation Anywhere Files\Automation Anywhere\\My Tasks\\DAPI Template AA2\\N00XX\\1.O365Login\\Temps\\']
# }

## AA 2.Office365Loggin Config

# config = {
#     'BASE_DIR':os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
#     'RPA_TOOl':'AutomationAnywhere',
#     'AA_TASK_NAME':'2.Office365Loggin',
#     'LOG_PATH':f'C:\\Users\\{getpass.getuser()}\\Documents\\Automation Anywhere Files\\Automation Anywhere\\My Tasks\\DAPI Template AA2\\N00XX\\1.O365Login\\Logs\\',
#     'RPA_TASK_FOLDER':f'C:\\Users\\{getpass.getuser()}\\Documents\\Automation Anywhere Files\\Automation Anywhere\\My Tasks\\DAPI Template AA2\\N00XX\\1.O365Login\\',
#     'TEST_RESULTS_FOLDER': [f'']
# }

## AA 3.sendEmails Config

config = {
    'BASE_DIR':os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'RPA_TOOl':'AutomationAnywhere',
    'AA_TASK_NAME':'3.sendEmails',
    'LOG_PATH':f'C:\\Users\\{getpass.getuser()}\\Documents\\Automation Anywhere Files\\Automation Anywhere\\My Tasks\\DAPI Template AA2\\N00XX\\1.O365Login\\Logs\\',
    'RPA_TASK_FOLDER':f'C:\\Users\\{getpass.getuser()}\\Documents\\Automation Anywhere Files\\Automation Anywhere\\My Tasks\\DAPI Template AA2\\N00XX\\1.O365Login\\',
    'TEST_RESULTS_FOLDER': [f'C:\\Users\\{getpass.getuser()}\\Documents\\Automation Anywhere Files\\Automation Anywhere\\My Tasks\\DAPI Template AA2\\N00XX\\1.O365Login\\Temps\\']
}


if __name__=="__main__":
    pass
    print(config['BASE_DIR'])
