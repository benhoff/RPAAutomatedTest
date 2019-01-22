Feature: {{cookiecutter.Robot_task_feature_description}}

    Summary of this feature [Optional]

    Background: There are no residual files of any previous execution of {{cookiecutter.RPA_task_name}}{{cookiecutter.RPA_task_extension}}
        Given All the residual files have been deleted


    Scenario Outline: the robot should {{cookiecutter.Robot_task_feature_description}}
        Given is <testdata> in the temp folder

        Given Robot runs <task>

        When Robot do the: <first> process 
        And Robot do the: <second> process 
        And Robot do the: <third> process

        Then Robot should: <fourth>


        Examples:
        |   task                                                                 | testdata    | first                           | second                            | third                           | fourth                           |
        |   {{cookiecutter.RPA_task_name}}{{cookiecutter.RPA_task_extension}}    | testdata    | **what should be logged first** | **what should be logged second**  | **what should be logged third** | **what should be logged fourth** |
