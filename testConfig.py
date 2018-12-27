import os

config = {
    'BASE_DIR':os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'RPA_TOOl':'UIPath',
    'LOG_PATH':'C:\\Users\\ryzen2600x\\AppData\\Local\\UiPath\\Logs\\',
    'RPA_TASK_FOLDER':'C:\\jenkins\\workspace\\RPAAutomatedTest_master\\',
    'TEST_RESULTS_FOLDER': ['C:\\jenkins\\workspace\\RPAAutomatedTest_master\\giftList\\']
}

# config = {
#     'BASE_DIR':os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
#     'RPA_TOOl':'UIPath',
#     'LOG_PATH':'C:\\Users\\juan.restrepo\\AppData\\Local\\UiPath\\Logs\\',
#     'RPA_TASK_FOLDER':'C:\\Users\\juan.restrepo\\Desktop\\JC\\laboratory-solutions\\juan.restrepo\\Laboratory 2\\UI\\',
#     'TEST_RESULTS_FOLDER': ['C:\\Users\\juan.restrepo\\Desktop\\JC\\laboratory-solutions\\juan.restrepo\\Laboratory 2\\UI\\giftList\\']
# }

if __name__=="__main__":
    pass
    print(config['BASE_DIR'])
