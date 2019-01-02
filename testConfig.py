import os
import getpass

config = {
    'BASE_DIR':os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'RPA_TOOl':'UIPath',
    'LOG_PATH':f'C:\\Users\\{getpass.getuser()}\\AppData\\Local\\UiPath\\Logs\\',
    'RPA_TASK_FOLDER':f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}\\RPAAutomatedTest_dev\\',
    'TEST_RESULTS_FOLDER': ['giftList\\']
}

if __name__=="__main__":
    pass
    print(config['BASE_DIRO'])
