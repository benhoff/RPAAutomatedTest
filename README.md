# RPA Automated Test 🙈

Cookiecutter template for the fast implementation of automated BDD tests for RPA projects or RPA tasks, focused mainly for a TDD methodology in RPA, for now only available for UIPath and Automation Anywhere.

This allow to create in a fast and easy way automated functional tests for RPA projects or little RPA tasks, this was created because unittesting doesnt have sense in the RPA world, every task in RPA cannot be insolated as a single responsability activity, so every task is micro functional part of a bot and can be tested like a little functional component of an application.

## Getting Started

This template was created in python and can be downloaded through [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/readme.html) 

### How this works

* The test starts a bot using the windows command line.
* The test starts to read in runtime the bot execution log file specified in LOG_PATH (inside configuration file of the test).
* The test tail the log waiting for the logs specified in {{mytaks}}.feature file, if the test find the log that he is looking for we can consider that this step is passed and he starts to wait for the next step log.
* The test stop the execution if he find the word "error" inside the log and considers as failed the test.

### Prerequisites

[Python](https://www.python.org/) 3.6 or above and PIP.

[Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/readme.html): can install cookiecutter using:

```
  pip install cookiecutter
```

### Using

To create a RPA Automated test project, just need to create the project through Cookiecutter using:

```
  https://github.com/petoandroide/RPAAutomatedTest/ -c template
```
This ask for some data for the project creation:
  * Project_name: test project name
  * RPA_tool: RPA tool used in this project (UIPart, AutomationAnywhere supported)
  * RPA_task_extension: Extension of the robot files(XAML, ATMX)
  * RPA_task_name: Name of the task to test
  * Robot_task_feature_description: Description about what the robot should do
  * Task_dir_folder, robot_outputs_folder, log_file_path, test_resources_dir_folder: This can be configurated after the project          creation in the project config file

This should create a project with this tree structure:

    📦excel Writer task
     ┣ 📂reports
     ┃ ┗ 📜.temp
     ┣ 📂resources
     ┃ ┣ 📂drivers
     ┃ ┃ ┗ 📜.temp
     ┃ ┗ 📂fixtures
     ┃ ┃ ┗ 📜.temp
     ┣ 📂test
     ┃ ┣ 📂abilities
     ┃ ┃ ┣ 📜customAbilities.py
     ┃ ┃ ┗ 📜defaultAbilities.py
     ┃ ┣ 📂interactions
     ┃ ┃ ┣ 📜customInteractions.py
     ┃ ┃ ┗ 📜defaultInteractions.py
     ┃ ┣ 📂questions
     ┃ ┃ ┣ 📜defaultQuestions.py
     ┃ ┃ ┗ 📜excelReaderQuestions.py
     ┃ ┣ 📂steps
     ┃ ┃ ┣ 📜environmentSteps.py
     ┃ ┃ ┣ 📜mytaskSteps.py
     ┃ ┃ ┗ 📜robotRunRPATasks.py
     ┃ ┣ 📂tasks
     ┃ ┃ ┣ 📜customTasks.py
     ┃ ┃ ┗ 📜defaultTasks.py
     ┃ ┣ 📂test_resources
     ┃ ┃ ┣ 📂features
     ┃ ┃ ┃ ┣ 📜excelReader.feature
     ┃ ┃ ┃ ┣ 📜excelWriter.feature
     ┃ ┃ ┃ ┣ 📜LogStalker.feature
     ┃ ┃ ┃ ┣ 📜mytask.feature
     ┃ ┃ ┃ ┣ 📜office365Loggin.feature
     ┃ ┃ ┃ ┗ 📜sendEmails.feature
     ┃ ┃ ┣ 📂testdata1
     ┃ ┃ ┃ ┣ 📜row_4.txt
     ┃ ┃ ┃ ┣ 📜row_5.txt
     ┃ ┃ ┃ ┣ 📜row_6.txt
     ┃ ┃ ┃ ┣ 📜row_7.txt
     ┃ ┃ ┃ ┣ 📜row_8.txt
     ┃ ┃ ┃ ┗ 📜row_9.txt
     ┃ ┃ ┣ 📂testdata2
     ┃ ┃ ┃ ┗ 📜row_4.txt
     ┃ ┃ ┗ 📂testdata3
     ┃ ┃ ┃ ┣ 📜Mails1.xlsx
     ┃ ┃ ┃ ┗ 📜Mails2.xlsx
     ┃ ┣ 📜.flake8
     ┃ ┣ 📜actor.py
     ┃ ┗ 📜logDriver.py
     ┣ 📂utils
     ┃ ┗ 📜fileUtils.py
     ┣ 📜.gitignore
     ┣ 📜Pipfile
     ┗ 📜testConfig.py

There are some custom*.py and default*.py files, the default*.py files contain code ready to test the majority of the RPA tasks in a basic way (tailing and waiting the logs inside the log file), also contains a test\test_resources\features{{taskname}}.feature, this is a [Gherkin BDD File](https://behave.readthedocs.io/en/latest/philosophy.html#the-gherkin-language) that describe the behavior of a bot, this allows to test the bot against the behavior described in the file:

'''

    Feature: nothing

    Summary of this feature [Optional]

    Background: There are no residual files of any previous execution of mytask.xaml
        Given All the residual files have been deleted


    Scenario Outline: the robot should nothing
        Given is <testdata> in the temp folder

        Given Robot runs <task>

        When Robot do the: <first> process 
        And Robot do the: <second> process 
        And Robot do the: <third> process

        Then Robot should: <fourth>


        Examples:
        |   task           | testdata    | first                           | second                            | third                           | fourth                           |
        |   mytask.xaml    | testdata    | **what should be logged first** | **what should be logged second**  | **what should be logged third** | **what should be logged fourth** |

'''

For default the cookiecutter template creates this {{taskname}}.feature file that treats the every step of the bot as a "process", you can customize and edit this file writing your own steps description.

*Note: if you connect this with a CI tool, your reports gonna be parsed with the text in the {{taskname}}.feature file*

#### Test config

You need to complete the test configuration in the *testConfig.py* file:

```
  import os
  import getpass

  config = {
      'BASE_DIR':os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
      'RPA_TOOl':'UIPath',
      'AA_TASK_NAME':'mytask',
      'LOG_PATH':'',
      'RPA_TASK_FOLDER':'',
      'TEST_RESOURCES_FOLDER':'\\excel Writer task\\test\\test_resources\\',
      'TEST_RESULTS_FOLDER': ['']
  }
```

'LOG_PATH' and 'RPA_TASK_FOLDER' are required.

### Test Dependencies

Test dependencies for default are in the Pipfile, you can add another or simply change to the classic requirements.txt file for your python virtual env:

```

    [[source]]
    name = "pypi"
    url = "https://pypi.org/simple"
    verify_ssl = true

    [dev-packages]
    pandas = "*"
    xlrd = "*"
    flake8 = "*"

    [packages]
    behave = "==1.2.6"
    behave2cucumber = "==1.0.3"
    junit2html = "==22"
    parse = "==1.9.0"
    psutil = "==5.4.8"
    six = "==1.12.0"
    parse_type = "==0.4.2"

    [requires]
    python_version = "3.7"
  
  
```

Install this dependencies using:

```
  Pipenv install
```

Or...

```
pip install -r requirements.txt
```

## Running the tests

Run your tests using behave and the folder where your test are writed:

```
behave test
```

## Externar dependencies

* [Behave](https://behave.readthedocs.io/en/latest/) - BDD Test runner for Python
* [Pipenv](https://pipenv.readthedocs.io/en/latest/) - Dependency Management, Python Dev Workflow for Humans

